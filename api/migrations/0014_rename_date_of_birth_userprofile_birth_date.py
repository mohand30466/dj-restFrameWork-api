# Generated by Django 3.2.6 on 2021-08-17 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='Date_of_birth',
            new_name='birth_date',
        ),
    ]