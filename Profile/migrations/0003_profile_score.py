# Generated by Django 3.0.2 on 2020-02-07 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_profile_isprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='score',
            field=models.FloatField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]