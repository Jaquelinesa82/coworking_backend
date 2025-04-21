from django.db import models
from auth_app.models import CustomUser
from rooms.models import Room


class Participant(models.Model):
    ROLE_CHOICES = [
        ('host', 'Host'),
        ('moderator', 'Moderator'),
        ('speaker', 'Speaker'),
        ('viewer', 'Viewer'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')
    joined_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active', choices=[('active', 'active'), ('inactive', 'inactive')])

    class Meta:
        unique_together = ('user', 'room')

    def __str__(self):
        return f'{self.user.email} em {self.room.name} como {self.role}'
