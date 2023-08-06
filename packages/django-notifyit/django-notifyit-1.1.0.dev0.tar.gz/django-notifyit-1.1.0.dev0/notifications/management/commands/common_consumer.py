from django.core.management.base import BaseCommand, CommandError
from notifications.consumers import Common
from notifications.connection import Connection
import pika


connection = Connection()
common_consumer = Common(connection)

class Command(BaseCommand):
    help = 'This command will run all Consumers'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):

        try:
            common_consumer.consume()
        except (pika.exceptions.StreamLostError, pika.exceptions.ChannelWrongStateError) as e:
            connection.reconnect()
            common_consumer.channel = connection.channel
            common_consumer.consume()
