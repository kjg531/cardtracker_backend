# Generated by Django 3.0.10 on 2020-10-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_auto_20201030_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='tracked',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
