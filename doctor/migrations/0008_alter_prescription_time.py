# Generated by Django 4.1.1 on 2022-10-01 17:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_remove_patientquery_qrimage_prescription_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='time',
            field=models.TimeField(max_length=100, verbose_name=datetime.time(23, 41, 14, 125574)),
        ),
    ]
