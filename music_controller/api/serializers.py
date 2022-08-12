from rest_framework import serializers
from .model import Room

clas RoomSerializer(serializer.Modelserializer):
class Meta:
    model = Room
    fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at',)
    