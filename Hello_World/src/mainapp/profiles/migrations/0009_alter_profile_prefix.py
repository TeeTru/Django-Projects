# Generated by Django 4.0.6 on 2022-07-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(choices=[('Dr', 'Dr'), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Ms', 'Ms')], max_length=4),
        ),
    ]
