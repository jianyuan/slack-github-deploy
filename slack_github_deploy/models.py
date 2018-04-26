from django.db import models
from social_django.models import UserSocialAuth


class SlackTeam(models.Model):
    team_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    social_users = models.ManyToManyField(UserSocialAuth)


class SlackBot(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    access_token = models.CharField(max_length=255)
    team = models.ForeignKey(SlackTeam, on_delete=models.PROTECT)
