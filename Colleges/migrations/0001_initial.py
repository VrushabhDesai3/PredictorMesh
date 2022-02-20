# Generated by Django 3.0.2 on 2020-01-13 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pictures')),
                ('desc', models.TextField()),
                ('fees', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
