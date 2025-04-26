from django.db import models
from auth_app.models import CustomUser
import uuid
from django.db.models import JSONField
from django.utils.translation import gettext_lazy as _


class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Nome da sala'))
    creator = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name=_('Criador da sala'))
    participants = models.ManyToManyField(
        CustomUser, through='participant.Participant', related_name='participating_rooms', verbose_name=_('Participantes'))
    start_time = models.TimeField()
    end_time = models.TimeField()
    room_code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name=_('Código da sala'))
    description = models.TextField(blank=True, null=True, verbose_name=_('Descrição'))
    category = models.CharField(
        max_length=20,
        choices=[('Reunião', 'Reunião'), ('Evento', 'Evento'), ('Networking', 'Networking')],
        default='Reunião', verbose_name=_('Categoria')
    )
    privacy = models.CharField(
        max_length=20,
        choices=[('public', 'Pública'), ('private', 'Privada')],
        default='private'
    )
    is_active = models.BooleanField(default=True, verbose_name=_('Está ativa'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criada em'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Atualizada em'))
    
    def __str__(self):
        return self.name
    
    
class Tool(models.Model):
    name = models.CharField(max_length=20, verbose_name=_('Nome da ferramenta'))
    tool_type = models.CharField(max_length=20, choices=[('interactive', 'Interactive'), ('visual', 'Visual')], verbose_name=_('Tipo da ferramenta'))
    room = models.ForeignKey(Room, related_name='tools', on_delete=models.CASCADE, verbose_name=_('Sala'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    

class Event(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('Título do evento'))
    event_id = models.ForeignKey(Room, related_name='events', on_delete=models.CASCADE, verbose_name=_('Sala'))
    description = models.TextField(verbose_name=_('Descrição do evento'))
    event_type = models.CharField(max_length=20, choices=[('palestra', 'Palestra'), ('workshop', 'Workshop'), ('webinar', 'Webinar')])
    event_date = models.DateField(verbose_name=_('Data do evento'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Criado em'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Atualizado em'))
    
    def __str__(self):
        return self.title
