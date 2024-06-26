# Generated by Django 4.1.1 on 2022-09-24 16:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('medicine', '0002_alter_patientdata_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdata',
            name='time',
            field=models.TimeField(max_length=100, verbose_name=datetime.time(22, 8, 42, 461142)),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=100)),
                ('mbbs', models.CharField(max_length=1000)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('dob', models.DateField()),
                ('address', models.TextField(max_length=2000)),
                ('nationality', models.CharField(max_length=1000)),
                ('bio', models.TextField(max_length=2000)),
                ('image', models.ImageField(default='default.jpg', upload_to='images/profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
