
import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Colleges', '0002_college_clglink'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='courses',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, default=[[1,2],[3,4]], size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='college',
            name='cutOff',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='college',
            name='rank',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
