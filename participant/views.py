from rest_framework import viewsets
from .models import Participant
from .serializers import ParticipantSerializer


class ParticipantViewSet(viewsets.ModelViewSet):
    serializer = Participant.objects.all()
    serializer_class = ParticipantSerializer
