from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CardSerializer
from .models import Card
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['sport', 'year', 'brand', 'program', 'card_set', 'number',
                        'name', 'team', 'sequence', 'tracked']
    search_fields = ['name', 'team', 'brand', 'program', 'card_set']
    ordering_fields = '__all__'
