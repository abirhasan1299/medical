# Generated by Django 4.1.1 on 2022-09-30 17:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_alter_prescription_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientquery',
            name='qrimage',
        ),
        migrations.AddField(
            model_name='prescription',
            name='email',
            field=models.EmailField(default=2, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='prescription',
            name='qrimage',
            field=models.ImageField(default='default.jpg', upload_to='images/qrcode'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='time',
            field=models.TimeField(max_length=100, verbose_name=datetime.time(23, 32, 26, 617562)),
        ),
    ]
