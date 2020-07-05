from django.shortcuts import render
from .models import ActivityPeriod, User
from .serializers import Activityserializer, Userserializer
from rest_framework import viewsets
# Create your views here.

class Userapi(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer

class Activityapi(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = Activityserializer