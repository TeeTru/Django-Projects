# Generated by Django 4.0.6 on 2022-07-30 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0011_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(choices=[('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Mr', 'Mr'), ('Dr', 'Dr')], max_length=4),
        ),
    ]
