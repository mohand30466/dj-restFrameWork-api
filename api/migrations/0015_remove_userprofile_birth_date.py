# Generated by Django 3.2.6 on 2021-08-17 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_rename_date_of_birth_userprofile_birth_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birth_date',
        ),
    ]
