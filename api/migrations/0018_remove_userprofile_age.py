# Generated by Django 3.2.6 on 2021-08-17 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_userprofile_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='age',
        ),
    ]
