import pika
from rest_framework import serializers

from notifications.connection import Connection
from notifications.models import Notification
from notifications.producer import Publisher


class NotificationSerializer(serializers.ModelSerializer):

    status = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Notification
        fields = '__all__'

    def create(self, validated_data):
        instance = super().create(validated_data)

        connection = Connection()
        publisher = Publisher(connection)
        try:
            publisher.publish(validated_data)
        except (pika.exceptions.StreamLostError, pika.exceptions.ChannelWrongStateError) as e:
            connection.reconnect()
            publisher.channel = connection.channel
            publisher.publish(validated_data)
        except Exception as e:
            return instance

        instance.status = "Published"
        instance.save()
        return instance

    # def update(self, instance, validated_data):
    #     instance = super().update(instance, validated_data)
    #     instance.status = "Not Published"

    #     connection = Connection()
    #     publisher = Publisher(connection)
    #     try:
    #         publisher.publish(instance)
    #     except (pika.exceptions.StreamLostError, pika.exceptions.ChannelWrongStateError) as e:
    #         connection.reconnect()
    #         publisher.channel = connection.channel
    #         publisher.publish(instance)

    #     instance.status = "Published"
    #     return instance
