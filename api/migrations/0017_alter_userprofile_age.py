# Generated by Django 3.2.6 on 2021-08-17 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_userprofile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(),
        ),
    ]
