import pika
import json

HEARTBEAT = 60
BLOCKED_CONNECTION_TIMEOUT = 200


class SingletonMetaclass(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        assert not (args or kwargs), 'Singleton should not accept arguments'

        if isinstance(cls._instance, cls):
            return cls._instance
        else:
            cls._instance = super(SingletonMetaclass, cls).__call__()
            return cls._instance


class Connection(metaclass=SingletonMetaclass):

    def __init__(self):
        print("Creating new connection..")
        self.parameters = pika.ConnectionParameters('localhost', heartbeat=HEARTBEAT, \
                                                    blocked_connection_timeout=BLOCKED_CONNECTION_TIMEOUT)
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

    def reconnect(self):
        print("Reconnection..")
        self.__init__()
