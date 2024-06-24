# Introduction

Welcome to the Cartrack Public Repository. This repository demonstrates how to retrieve messages from the Cartrack queue efficiently. Your suggestions for improvements are highly appreciated.

## ⚙️ Pre-requisites

Ensure you have Python 3.10.4 installed.

After cloning this repository, perform the following steps:

* Create a virtual environment: Execute `python3 -m venv venv`
* Activate the virtual environment: Run `source venv/bin/activate`
* Install the required packages: Use `pip3 install -r requirements.txt`

## How to Use

To begin, set your environment variables accordingly. Cartrack will provide you with the necessary credentials, which include:

* Queue Username
* Queue Password
* Queue Hostname

Note that the queue name will correspond to the queue username.

Follow these steps to configure your environment:

1. Duplicate the environment file: `cp .env-example .env`
2. Edit the new environment file: `vim .env`

Below is an example of how your `.env` file should look:

```sh
# Environment Variables

# Example
MQ_USERNAME='username'
MQ_PASSWORD='password'
MQ_HOSTNAME='hostname'
```

## Result

Execute `python3 consume.py` to retrieve messages from your queue and save them to a JSON file. Feel free to modify the script to suit your specific requirements.

## 📝 Notes

Please be aware of the following:

* Queues are durable and will remain active even after disconnection.
* Queues possess a Time To Live (TTL) of 5 hours.
* Queues are non-exclusive, allowing multiple consumers to connect simultaneously.

## Resources

* [RabbitMQ](https://www.rabbitmq.com/)
* [Pika](https://pika.readthedocs.io/en/stable/)
* [Python-dotenv](https://pypi.org/project/python-dotenv/)
