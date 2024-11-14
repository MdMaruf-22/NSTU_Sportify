from rest_framework import viewsets
from .models import *
from .serializers import *

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class RepresentativeViewSet(viewsets.ModelViewSet):
    queryset = Representative.objects.all()
    serializer_class = RepresentativeSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class MatchDetailSet(viewsets.ModelViewSet):
    queryset = Matchdetails.objects.all()
    serializer_class = MatchSerializer

class CarromViewSet(viewsets.ModelViewSet):
    queryset = Carrom.objects.all()
    serializer_class = CarromSerializer

class HandBall(viewsets.ModelViewSet):
    queryset = Handball.objects.all()
    serializer_class = HandballSerializer

