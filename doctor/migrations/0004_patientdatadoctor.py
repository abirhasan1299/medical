# Generated by Django 4.1.1 on 2022-09-25 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_rename_query_patientquery_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientDataDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('symptoms', models.TextField(max_length=2000)),
                ('mobile', models.IntegerField()),
                ('disease', models.CharField(max_length=2000)),
                ('advice', models.TextField(blank=True, max_length=5000, null=True)),
                ('investigation', models.TextField(blank=True, max_length=5000, null=True)),
                ('time', models.TimeField(max_length=100, verbose_name=datetime.time(2, 29, 10, 824455))),
                ('med_types_1', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_1', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_1', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_1', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_1', models.CharField(blank=True, max_length=100, null=True)),
                ('day_1', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_2', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_2', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_2', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_2', models.CharField(blank=True, max_length=100, null=True)),
                ('day_2', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_3', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_3', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_3', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_3', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_3', models.CharField(blank=True, max_length=100, null=True)),
                ('day_3', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_4', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_4', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_4', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_4', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_4', models.CharField(blank=True, max_length=100, null=True)),
                ('day_4', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_5', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_5', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_5', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_5', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_5', models.CharField(blank=True, max_length=100, null=True)),
                ('day_5', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_6', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_6', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_6', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_6', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_6', models.CharField(blank=True, max_length=100, null=True)),
                ('day_6', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_7', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_7', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_7', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_7', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_7', models.CharField(blank=True, max_length=100, null=True)),
                ('day_7', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_8', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_8', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_8', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_8', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_8', models.CharField(blank=True, max_length=100, null=True)),
                ('day_8', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_9', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_9', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_9', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_9', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_9', models.CharField(blank=True, max_length=100, null=True)),
                ('day_9', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_10', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_10', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_10', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_10', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_10', models.CharField(blank=True, max_length=100, null=True)),
                ('day_10', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_11', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_11', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_11', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_11', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_11', models.CharField(blank=True, max_length=100, null=True)),
                ('day_11', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_12', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_12', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_12', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_12', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_12', models.CharField(blank=True, max_length=100, null=True)),
                ('day_12', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_13', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_13', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_13', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_13', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_13', models.CharField(blank=True, max_length=100, null=True)),
                ('day_13', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_14', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_14', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_14', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_14', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_14', models.CharField(blank=True, max_length=100, null=True)),
                ('day_14', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_15', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_15', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_15', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_15', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_15', models.CharField(blank=True, max_length=100, null=True)),
                ('day_15', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_16', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_16', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_16', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_16', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_16', models.CharField(blank=True, max_length=100, null=True)),
                ('day_16', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_17', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_17', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_17', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_17', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_17', models.CharField(blank=True, max_length=100, null=True)),
                ('day_17', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_18', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_18', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_18', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_18', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_18', models.CharField(blank=True, max_length=100, null=True)),
                ('day_18', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_19', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_19', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_19', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_19', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_19', models.CharField(blank=True, max_length=100, null=True)),
                ('day_19', models.CharField(blank=True, max_length=100, null=True)),
                ('med_types_20', models.CharField(blank=True, choices=[('Cap', 'Cap'), ('Syp', 'Syp'), ('Tab', 'Tab'), ('Sus', 'Sus'), ('Oral', 'Oral'), ('Injec', 'Injec')], max_length=100, null=True)),
                ('grp_20', models.CharField(blank=True, max_length=1000, null=True)),
                ('brand_20', models.CharField(blank=True, max_length=1000, null=True)),
                ('taken_time_20', models.CharField(blank=True, choices=[('1+1+1', '1+1+1'), ('1+0+1', '1+0+1'), ('1+0+0', '1+0+0'), ('0+1+1', '0+1+1'), ('0+1+0', '0+1+0'), ('0+0+1', '0+0+1'), ('1+1+0', '1+1+0'), ('0+0+0', '0+0+0')], max_length=100, null=True)),
                ('qty_20', models.CharField(blank=True, max_length=100, null=True)),
                ('day_20', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]