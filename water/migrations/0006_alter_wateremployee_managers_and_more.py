# Generated by Django 4.0.3 on 2022-04-30 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0005_alter_wateremployee_table'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='wateremployee',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='waterbillinfo',
            name='prev_reading',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=50),
        ),
    ]
