# Generated by Django 3.0.2 on 2020-02-29 17:32

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('desc2', models.TextField()),
                ('coreSubjects', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, size=None)),
                ('universities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=5000), blank=True, size=None)),
            ],
        ),
    ]