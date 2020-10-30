from django.db import models

from cardtracker_backend.players.models import Player


class Card(models.Model):
    sport = models.CharField(max_length=100, null=True)
    year = models.IntegerField(default=2019)
    brand = models.CharField(max_length=100, null=True)
    program = models.CharField(max_length=100, null=True)
    card_set = models.CharField(max_length=100, null=True)
    number = models.IntegerField(null=True)
    name = models.CharField(max_length=10000, null=True)
    team = models.CharField(max_length=10000, null=True)
    sequence = models.IntegerField(null=True)
    tracked = models.BooleanField(default=False)
    search_url = models.URLField(max_length=100, null=True)


class CardSale(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    link = models.URLField(max_length=100, null=True)
    purchase_type = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    bids = models.IntegerField(null=True)
    shipping_cost = models.IntegerField(null=True)
    image = models.URLField(max_length=100, null=True)
