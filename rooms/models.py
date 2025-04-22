from django.db import models
from auth_app.models import CustomUser
import uuid
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _


class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Nome da sala'))
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    participants = models.ManyToManyField(
        CustomUser, through='participant.Participant', related_name='participating_rooms')
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
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
    
    
class Tool(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Nome da ferramenta'))#(Ex: quadro branco, chat, tela de compartilhamento
    tool_type = models.CharField(max_length=20, choices=[('interactive', 'Interactive'), ('visual', 'Visual')])
    room = models.ForeignKey(Room, related_name='tools', on_delete=models.CASCADE, verbose_name=_('Sala'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Event(models.Model):
    title = models.CharField(max_length=50)
    room = models.ForeignKey(Room, related_name='events', on_delete=models.CASCADE, verbose_name=_('Evento'))
    description = models.TextField()
    event_type = models.CharField(max_length=20, choices=[('palestra', 'Palestra'), ('workshop', 'Workshop'), ('webinar', 'Webinar')])
    event_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
