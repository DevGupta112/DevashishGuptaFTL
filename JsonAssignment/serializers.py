from rest_framework import serializers
from .models import ActivityPeriod, User

class Activityserializer(serializers.ModelSerializer):
    class Meta:
        model=ActivityPeriod
        fields="__all__"

class Userserializer(serializers.ModelSerializer):
    activity=Activityserializer(read_only=True, many=True)
    class Meta:
        model=User
        fields="__all__"