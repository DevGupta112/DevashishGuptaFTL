from django.db import models

# Create your models here.
class User(models.Model):
    uid=models.CharField(max_length=2555, primary_key=True)
    real_name=models.CharField(max_length=2555, null=True, blank=True)
    tz=models.CharField(max_length=2555, null=True, blank=True)


class ActivityPeriod(models.Model):
    start_time=models.CharField(max_length=2555, null=True, blank=True)
    end_time=models.CharField(max_length=2555, null=True, blank=True)
    uid=models.ForeignKey(User, related_name='activity', on_delete=models.CASCADE)