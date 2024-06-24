import os
import pika
import re
import logging
from dotenv import load_dotenv
from contextlib import contextmanager

# Load environment variables
load_dotenv()

# Retrieve MQ credentials from environment variables
MQ_USERNAME = os.getenv("MQ_USERNAME")
MQ_PASSWORD = os.getenv("MQ_PASSWORD")
MQ_HOSTNAME = os.getenv("MQ_HOSTNAME")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@contextmanager
def open_connection():
    """Context manager to ensure the RabbitMQ connection is closed properly."""
    params = pika.URLParameters(f"amqps://{MQ_USERNAME}:{MQ_PASSWORD}@{MQ_HOSTNAME}")
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    try:
        yield channel
    finally:
        logger.info("Closing connection... please wait")
        connection.close()
        logger.info("Connection closed.")


@contextmanager
def open_log_file():
    """Context manager to ensure the log file is closed properly."""
    with open(f"./logs/{MQ_USERNAME}.log", "a") as file:
        yield file


def callback(channel, method_frame, header_frame, body, file):
    """Callback function to handle incoming messages."""
    # Extract JSON-like content from the message body
    json_content = re.search(r"{.*}", str(body))
    if json_content:
        file.write(json_content.group() + "\n")
    else:
        logger.warning("No JSON content found in the message.")


def main():
    with open_connection() as channel, open_log_file() as file:
        channel.basic_consume(
            queue=MQ_USERNAME,
            on_message_callback=lambda ch, method, properties, body: callback(
                ch, method, properties, body, file
            ),
            auto_ack=True,
        )

        logger.info("Starting message consumption. Press CTRL+C to stop.")
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            logger.info("Stopped by user.")


if __name__ == "__main__":
    main()
