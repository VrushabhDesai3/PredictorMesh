# Generated by Django 3.0.2 on 2020-03-14 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0002_course_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='link',
            field=models.CharField(default='hi', max_length=100),
            preserve_default=False,
        ),
    ]
