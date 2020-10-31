from rest_framework import serializers
from .models import Card
# Serializers define the API representation.


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['sport', 'year', 'brand', 'program', 'card_set', 'number',
                  'name', 'team', 'sequence', 'tracked', 'search_url']
