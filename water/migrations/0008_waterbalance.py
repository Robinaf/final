# Generated by Django 4.0.3 on 2022-05-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0007_alter_waterbillinfo_date_alter_waterbillinfo_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaterBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=50)),
            ],
        ),
    ]