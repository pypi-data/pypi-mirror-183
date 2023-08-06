import time
import json
from pika.exchange_type import ExchangeType
from abc import ABC, abstractmethod


class Consumer(ABC):

    def __init__(self, connection):
        self.connection = connection
        self.channel = connection.channel

    def consume(self):
        pass

    def on_message_received(self, ch, method, properties, body):
        pass


class Common:

    def __init__(self, connection):
        self.connection = connection
        self.channel = connection.channel

    def consume(self):
        self.channel.exchange_declare(exchange='topicexchange', exchange_type=ExchangeType.topic)
        queue = self.channel.queue_declare(queue='', exclusive=True)

        self.channel.queue_bind(exchange='topicexchange', queue=queue.method.queue, routing_key='#.common')
        self.channel.queue_bind(exchange='topicexchange', queue=queue.method.queue, routing_key='all')

        self.channel.basic_consume(queue=queue.method.queue, auto_ack=False,
            on_message_callback=self.on_message_received)

        print(f"Common Starts Consuming...")

        self.channel.start_consuming()

    def on_message_received(self, ch, method, properties, body):
        print(f"Common received new message: {json.loads(body)}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"Common finished processing and acknowledged message")


class ChatIt:

    def __init__(self, connection):
        self.connection = connection
        self.channel = connection.channel

    def consume(self):
        self.channel.exchange_declare(exchange='topicexchange', exchange_type=ExchangeType.topic)
        queue = self.channel.queue_declare(queue='', exclusive=True)

        self.channel.queue_bind(exchange='topicexchange', queue=queue.method.queue, routing_key='#.chatit')
        self.channel.queue_bind(exchange='topicexchange', queue=queue.method.queue, routing_key='all')

        self.channel.basic_consume(queue=queue.method.queue, auto_ack=False,
            on_message_callback=self.on_message_received)

        print(f"ChatIt Starts Consuming...")

        self.channel.start_consuming()

    def on_message_received(self, ch, method, properties, body):
        print(f"ChatIt received new message: {json.loads(body)}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"ChatIt finished processing and acknowledged message")


class PollIt:

    def __init__(self, connection):
        self.connection = connection
        self.channel = connection.channel

    def consume(self):
        self.channel.exchange_declare(exchange='topicexchange', exchange_type=ExchangeType.topic)
        queue = self.channel.queue_declare(queue='', exclusive=True)

        self.channel.queue_bind(exchange='topicexchange', queue=queue.method.queue, routing_key='#.pollit')
        self.channel.queue_bind(exchange='topicexchange', queue=queue.method.queue, routing_key='all')

        self.channel.basic_consume(queue=queue.method.queue, auto_ack=False,
            on_message_callback=self.on_message_received)

        print(f"PollIt Starts Consuming...")

        self.channel.start_consuming()

    def on_message_received(self, ch, method, properties, body):
        print(f"PollIt received new message: {json.loads(body)}")
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print(f"PollIt finished processing and acknowledged message")
