# Generated by Django 4.0.6 on 2022-08-01 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='intitial_deposit',
            new_name='initial_deposit',
        ),
    ]
