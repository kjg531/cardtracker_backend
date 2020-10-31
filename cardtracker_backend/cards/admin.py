from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource
from import_export.fields import Field
from .models import Card, CardSale


class CardResource(ModelResource):
    sport = Field(attribute='sport', column_name='Sport')
    brand = Field(attribute='brand', column_name='Brand')
    program = Field(attribute='program', column_name='Program')
    card_set = Field(attribute='card_set', column_name='Card Set')
    number = Field(attribute='number', column_name='Number')
    name = Field(attribute='name', column_name='Name')
    team = Field(attribute='team', column_name='Team')
    sequence = Field(attribute='sequence', column_name='Sequence')
    tracked = Field(attribute='tracked', column_name='Tracked')
    search_url = Field(attribute='search_url', column_name='Search URL')

    class Meta:
        model = Card


class CardAdmin(ImportExportModelAdmin):
    resource_class = CardResource
    list_filter = ['sport', 'year', 'brand', 'program', 'card_set',
                   'name', 'team', 'tracked']
    list_display = ('sport', 'year', 'brand', 'program', 'card_set', 'number',
                    'name', 'team', 'sequence', 'tracked', 'search_url')

    # def view_birth_date(self, obj):
    #     return obj.birth_date

    # view_birth_date.empty_value_display = '???'


admin.site.register(Card, CardAdmin)
admin.site.register(CardSale)
