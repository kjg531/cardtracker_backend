from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=50)


class Player(models.Model):
    name = models.CharField(max_length=200)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
