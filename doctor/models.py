from django.db import models
from PIL import Image
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import datetime

# Create your models here.
class patientQuery(models.Model):
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )
    name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=1000)
    age = models.IntegerField()
    height = models.CharField(max_length=100)
    gender = models.CharField(max_length=100,choices=GENDER)
    problem = models.TextField(max_length=5000)
    #qrimage =models.ImageField(default='default.jpg',upload_to='images/qrcode')

    def __str__(self):
        return self.name

class Prescription(models.Model):
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
    GENDER=(
        ('Male','Male'),
        ('Female','Female')
    )
    qrimage =models.ImageField(default='default.jpg',upload_to='images/qrcode')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=1000)
    gender =models.CharField(max_length=10,choices=GENDER)
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
    taken_time_1 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_1 = models.CharField(max_length=100, null=True, blank=True)
    day_1 = models.CharField(max_length=100, null=True, blank=True)
    #level-2
    med_types_2 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_2 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_2 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_2 = models.CharField(max_length=100, null=True, blank=True)
    day_2 = models.CharField(max_length=100, null=True, blank=True)
    #level-3
    med_types_3 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_3 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_3 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_3 = models.CharField(max_length=100, null=True, blank=True)
    day_3 = models.CharField(max_length=100, null=True, blank=True)
    #level-4
    med_types_4 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_4 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_4 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_4 = models.CharField(max_length=100, null=True, blank=True)
    day_4 = models.CharField(max_length=100, null=True, blank=True)
    #level-5
    med_types_5 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_5 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_5 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_5 = models.CharField(max_length=100, null=True, blank=True)
    day_5 = models.CharField(max_length=100, null=True, blank=True)
    #level-6
    med_types_6 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_6 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_6 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_6 = models.CharField(max_length=100, null=True, blank=True)
    day_6 = models.CharField(max_length=100, null=True, blank=True)
    #level-7
    med_types_7 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_7 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_7 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_7 = models.CharField(max_length=100, null=True, blank=True)
    day_7 = models.CharField(max_length=100, null=True, blank=True)
    #level-8
    med_types_8 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_8 = models.CharField(
        max_length=1000, null=True, blank=True)

    taken_time_8 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_8 = models.CharField(max_length=100, null=True, blank=True)
    day_8 = models.CharField(max_length=100, null=True, blank=True)
    #level-9
    med_types_9 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_9 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_9 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_9 = models.CharField(max_length=100, null=True, blank=True)
    day_9 = models.CharField(max_length=100, null=True, blank=True)
    #level-10
    med_types_10 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_10 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_10 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_10 = models.CharField(max_length=100, null=True, blank=True)
    day_10 = models.CharField(max_length=100, null=True, blank=True)
    #level-11
    med_types_11 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_11 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_11 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_11 = models.CharField(max_length=100, null=True, blank=True)
    day_11 = models.CharField(max_length=100, null=True, blank=True)
    #level-12
    med_types_12 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_12 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_12 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_12 = models.CharField(max_length=100, null=True, blank=True)
    day_12 = models.CharField(max_length=100, null=True, blank=True)
    #level-13
    med_types_13 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_13 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_13 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_13 = models.CharField(max_length=100, null=True, blank=True)
    day_13 = models.CharField(max_length=100, null=True, blank=True)
    #level-14
    med_types_14 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_14 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_14 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_14 = models.CharField(max_length=100, null=True, blank=True)
    day_14 = models.CharField(max_length=100, null=True, blank=True)
    #level-15
    med_types_15 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_15 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_15 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_15 = models.CharField(max_length=100, null=True, blank=True)
    day_15 = models.CharField(max_length=100, null=True, blank=True)
    #level-16
    med_types_16 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_16 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_16 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_16 = models.CharField(max_length=100, null=True, blank=True)
    day_16 = models.CharField(max_length=100, null=True, blank=True)
    #level-17
    med_types_17 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_17 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_17 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_17 = models.CharField(max_length=100, null=True, blank=True)
    day_17 = models.CharField(max_length=100, null=True, blank=True)
    #level-18
    med_types_18 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_18 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_18 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_18 = models.CharField(max_length=100, null=True, blank=True)
    day_18 = models.CharField(max_length=100, null=True, blank=True)
    #level-19
    med_types_19 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_19 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_19 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_19 = models.CharField(max_length=100, null=True, blank=True)
    day_19 = models.CharField(max_length=100, null=True, blank=True)
    #level-20
    med_types_20 = models.CharField(
        max_length=100, choices=TYPES, null=True, blank=True)
    grp_20 = models.CharField(
        max_length=1000, null=True, blank=True)
    taken_time_20 = models.CharField(
        max_length=100, choices=TIME, null=True, blank=True)
    qty_20 = models.CharField(max_length=100, null=True, blank=True)
    day_20 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        qr_identity = f'http://127.0.0.1:8000/doctor/search/?email={self.email}'
        qr_image = qrcode.make(qr_identity)
        canvas = Image.new('RGB',(400,400),'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        fname  = f'medbd-{self.name}-{self.mobile}'+'.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qrimage.save(fname,File(buffer),save=False)
        canvas.close()
        super().save(*args, **kwargs)