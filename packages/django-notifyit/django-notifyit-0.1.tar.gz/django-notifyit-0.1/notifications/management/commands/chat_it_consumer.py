from django.core.management.base import BaseCommand, CommandError
from notifications.consumers import ChatIt
from notifications.connection import Connection
import pika


connection = Connection()
chat_it_consumer = ChatIt(connection)

class Command(BaseCommand):
    help = 'This command will run all Consumers'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        try:
            chat_it_consumer.consume()
        except (pika.exceptions.StreamLostError, pika.exceptions.ChannelWrongStateError) as e:
            connection.reconnect()
            chat_it_consumer.channel = connection.channel
            chat_it_consumer.consume()
