# Generated by Django 4.0.3 on 2022-05-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('electric', '0004_alter_electricemployee_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
            ],
        ),
    ]
