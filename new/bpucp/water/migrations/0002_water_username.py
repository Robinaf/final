# Generated by Django 4.0.3 on 2022-03-26 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='water',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
