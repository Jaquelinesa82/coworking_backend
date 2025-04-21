from django.db import models
from auth_app.models import CustomUser
import uuid
from django.db.models import JSONField


class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome da sala')
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(
        CustomUser, through='participant.Participant', related_name='participating_rooms')
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    tools = models.JSONField(default=list, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(
        max_length=20,
        choices=[('Reunião', 'Reunião'), ('Evento', 'Evento'), ('Networking', 'Networking')],
        default='Reunião'
    )
    privacy = models.CharField(
        max_length=20,
        choices=[('public', 'Pública'), ('private', 'Privada')],
        default='private'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name