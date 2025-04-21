from rest_framework import serializers
from rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'last_name', 'description', 'created_at']