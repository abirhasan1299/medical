# Generated by Django 4.1.1 on 2022-09-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patientQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mobile', models.IntegerField()),
                ('email', models.EmailField(max_length=1000)),
                ('age', models.IntegerField()),
                ('height', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('query', models.TextField(max_length=5000)),
                ('image', models.ImageField(default='default.jpg', upload_to='images/profile')),
            ],
        ),
    ]
