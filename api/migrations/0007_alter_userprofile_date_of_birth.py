# Generated by Django 3.2.6 on 2021-08-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_userprofile_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='Date_of_birth',
            field=models.DateField(default=2020.0),
        ),
    ]
