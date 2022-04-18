# Generated by Django 4.0.3 on 2022-04-05 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_account_roles_account_role_delete_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Water_Admin'), (2, 'Electric_Admin'), (3, 'Water_Reader'), (4, 'Water_Technician'), (5, 'Electric_Reader'), (6, 'Electric_Technician'), (7, 'Customer')], null=True),
        ),
    ]
