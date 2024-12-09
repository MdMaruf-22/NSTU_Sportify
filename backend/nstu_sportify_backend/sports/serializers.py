from ast import Match
from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class RepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representative
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        

class CarromSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrom
        fields = '__all__'


class HandballSerializer(serializers.ModelSerializer):
    class Meta:
        model = Handball
        fields = '__all__'


class ChessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chess
        fields = '__all__'


class FootballSerializer(serializers.ModelSerializer):
    class Meta:
        model = Football
        fields = '__all__'


class CricketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cricket
        fields = '__all__'


class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class StandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standing
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class LiveScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livescore
        fields = '__all__'

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
