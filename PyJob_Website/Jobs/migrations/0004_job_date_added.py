# Generated by Django 4.0.2 on 2022-02-15 21:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0003_remove_email_id_alter_email_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 15, 21, 8, 52, 461804, tzinfo=utc)),
        ),
    ]