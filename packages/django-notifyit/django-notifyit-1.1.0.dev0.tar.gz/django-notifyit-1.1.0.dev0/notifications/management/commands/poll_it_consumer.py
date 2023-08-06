from django.core.management.base import BaseCommand, CommandError
from notifications.consumers import PollIt
from notifications.connection import Connection
import pika


connection = Connection()
poll_it_consumer = PollIt(connection)

class Command(BaseCommand):
    help = 'This command will run all Consumers'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        
        try:
            poll_it_consumer.consume()
        except (pika.exceptions.StreamLostError, pika.exceptions.ChannelWrongStateError) as e:
            connection.reconnect()
            poll_it_consumer.channel = connection.channel
            poll_it_consumer.consume()
