# Generated by Django 4.0.2 on 2022-02-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('contract', models.CharField(max_length=10, null=True)),
                ('location', models.CharField(max_length=50, null=True)),
                ('remote', models.CharField(max_length=50, null=True)),
                ('education_level', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=5000)),
                ('salary', models.IntegerField(null=True)),
                ('date_published', models.DateTimeField()),
                ('url', models.CharField(max_length=100)),
            ],
        ),
    ]
