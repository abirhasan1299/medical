# Generated by Django 4.1.1 on 2022-09-30 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0012_alter_patientdata_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='time',
            field=models.TimeField(max_length=100, verbose_name=datetime.time(23, 32, 26, 595791)),
        ),
    ]
