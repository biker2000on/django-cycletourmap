from django.contrib.auth.models import AbstractUser
from django.db import models


class Athlete(AbstractUser):
    id = models.UUIDField(primary_key=True)
    strava_id = models.IntegerField(blank=True, null=True)
    firstname = models.TextField(blank=True, null=True)
    lastname = models.TextField(blank=True, null=True)
    profile = models.TextField(blank=True, null=True)
    profile_medium = models.TextField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    date_preference = models.TextField(blank=True, null=True)
    measurement_preference = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "athlete"
