from pika.exchange_type import ExchangeType
import json


class Publisher:

    def __init__(self, connection):
        self.connection = connection
        self.channel = connection.channel

    def publish(self, data):
        self.channel.exchange_declare(exchange='topicexchange', exchange_type=ExchangeType.topic)
        self.channel.basic_publish(exchange='topicexchange', routing_key=data["routing_key"], body=json.dumps(data, default=str))
        print(f"sent message: {data}")
