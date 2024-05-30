from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class UserProfile(models.Model):
    STATUS = (
        ('Online','Online'),
        ('Offline','Offline'),
    )
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100,choices=STATUS)
    mbbs = models.CharField(max_length=1000)
    gender = models.CharField(max_length=100,choices=GENDER)
    dob = models.DateField()
    address = models.TextField(max_length=2000)
    nationality = models.CharField(max_length=1000)
    bio = models.TextField(max_length=2000)
    image =models.ImageField(default = 'default.jpg', upload_to='images/profile')
    def __str__(self):
        return self.user.username
    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width >300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class AddMedicine(models.Model):

    name = models.CharField(max_length=500)
    group = models.CharField(max_length=500)
    expire = models.DateField()
    price = models.CharField(max_length=100)
    uses = models.TextField(max_length=50000)

    def __str__(self):
        return self.name

import datetime
class PatientData(models.Model):
    TYPES = (
        ('Cap','Cap'),
        ('Syp','Syp'),
        ('Tab','Tab'),
        ('Sus','Sus'),
        ('Oral','Oral'),
        ('Injec','Injec'),
    )
    TIME = (
        ('1+1+1', '1+1+1'),
        ('1+0+1', '1+0+1'),
        ('1+0+0', '1+0+0'),
        ('0+1+1', '0+1+1'),
        ('0+1+0', '0+1+0'),
        ('0+0+1', '0+0+1'),
        ('1+1+0', '1+1+0'),
        ('0+0+0', '0+0+0'),
    )
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=10)
    date = models.DateField()
    symptoms = models.TextField(max_length=2000)
    mobile = models.IntegerField()
    disease = models.CharField(max_length=2000)
    advice = models.TextField(max_length=5000, null=True, blank=True)
    investigation = models.TextField(max_length=5000, null=True, blank=True)
    time = models.TimeField(datetime.datetime.now().time(),max_length=100)
    #level-1
    med_types_1 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_1 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_1 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_1 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_1 = models.CharField(max_length=100, null=True, blank=True)
    day_1 = models.CharField(max_length=100, null=True, blank=True)
    #level-2
    med_types_2 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_2 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_2 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_2 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_2 = models.CharField(max_length=100, null=True, blank=True)
    day_2 = models.CharField(max_length=100, null=True, blank=True)
    #level-3
    med_types_3 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_3 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_3 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_3 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_3 = models.CharField(max_length=100, null=True, blank=True)
    day_3 = models.CharField(max_length=100, null=True, blank=True)
    #level-4
    med_types_4 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_4 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_4 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_4 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_4 = models.CharField(max_length=100, null=True, blank=True)
    day_4 = models.CharField(max_length=100, null=True, blank=True)
    #level-5
    med_types_5 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_5 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_5 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_5 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_5 = models.CharField(max_length=100, null=True, blank=True)
    day_5 = models.CharField(max_length=100, null=True, blank=True)
    #level-6
    med_types_6 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_6 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_6 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_6 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_6 = models.CharField(max_length=100, null=True, blank=True)
    day_6 = models.CharField(max_length=100, null=True, blank=True)
    #level-7
    med_types_7 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_7 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_7 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_7 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_7 = models.CharField(max_length=100, null=True, blank=True)
    day_7 = models.CharField(max_length=100, null=True, blank=True)
    #level-8
    med_types_8 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_8 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_8 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_8 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_8 = models.CharField(max_length=100, null=True, blank=True)
    day_8 = models.CharField(max_length=100, null=True, blank=True)
    #level-9
    med_types_9 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_9 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_9 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_9 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_9 = models.CharField(max_length=100, null=True, blank=True)
    day_9 = models.CharField(max_length=100, null=True, blank=True)
    #level-10
    med_types_10 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_10 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_10 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_10 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_10 = models.CharField(max_length=100, null=True, blank=True)
    day_10 = models.CharField(max_length=100, null=True, blank=True)
    #level-11
    med_types_11 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_11 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_11 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_11 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_11 = models.CharField(max_length=100, null=True, blank=True)
    day_11 = models.CharField(max_length=100, null=True, blank=True)
    #level-12
    med_types_12 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_12 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_12 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_12 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_12 = models.CharField(max_length=100, null=True, blank=True)
    day_12 = models.CharField(max_length=100, null=True, blank=True)
    #level-13
    med_types_13 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_13 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_13 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_13 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_13 = models.CharField(max_length=100, null=True, blank=True)
    day_13 = models.CharField(max_length=100, null=True, blank=True)
    #level-14
    med_types_14 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_14 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_14 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_14 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_14 = models.CharField(max_length=100, null=True, blank=True)
    day_14 = models.CharField(max_length=100, null=True, blank=True)
    #level-15
    med_types_15 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_15 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_15 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_15 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_15 = models.CharField(max_length=100, null=True, blank=True)
    day_15 = models.CharField(max_length=100, null=True, blank=True)
    #level-15
    med_types_15 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_15 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_15 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_15 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_15 = models.CharField(max_length=100, null=True, blank=True)
    day_15 = models.CharField(max_length=100, null=True, blank=True)
    #level-16
    med_types_16 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_16 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_16 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_16 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_16 = models.CharField(max_length=100, null=True, blank=True)
    day_16 = models.CharField(max_length=100, null=True, blank=True)
    #level-17
    med_types_17 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_17 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_17 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_17 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_17 = models.CharField(max_length=100, null=True, blank=True)
    day_17 = models.CharField(max_length=100, null=True, blank=True)
    #level-18
    med_types_18 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_18 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_18 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_18 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_18 = models.CharField(max_length=100, null=True, blank=True)
    day_18 = models.CharField(max_length=100, null=True, blank=True)
    #level-19
    med_types_19 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_19 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_19 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_19 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_19 = models.CharField(max_length=100, null=True, blank=True)
    day_19 = models.CharField(max_length=100, null=True, blank=True)
    #level-20
    med_types_20 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_20 = models.CharField(
        max_length=1000, null=True, blank=True)
    brand_20 = models.CharField(max_length=1000, null=True, blank=True)
    taken_time_20 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_20 = models.CharField(max_length=100, null=True, blank=True)
    day_20 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
