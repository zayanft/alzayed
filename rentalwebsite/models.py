from django.db import models

# Create your models here.
# Home Slide Models

class home_slide1(models.Model):
    headiline = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='homepage')

class home_slide2(models.Model):
    headiline = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='homepage')

class home_slide3(models.Model):
    headiline = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='homepage')
    

# EQUIPMENTS
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    image = models.ImageField(upload_to="equipments")
    EQUIPMENT_TYPES = (
        ('EXCAVATOR', 'EXCAVATOR'),
        ('CRANES', 'CRANES'),
        ('CLEANING EQUIPMENT', 'CLEANING EQUIPMENT'),
        ('LIFTING EQUIPMENT', "LIFTING EQUIPMENT"),
        ('TRUCK','TRUCK'),
        ('TANKER','TANKER'),
        ('POWER TOOLS','POWER TOOLS'),
        ('PUMP','PUMP'),
        ('CONSTRUCTION EQUIPMENTS','CONSTRUCTION EQUIPMENTS'),
    )
    type = models.CharField(max_length=50,choices=EQUIPMENT_TYPES, default='EXCAVATOR')

    title = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title

class Service(models.Model):
    image = models.ImageField(upload_to='services')
    title = models.CharField(max_length=50)
    description = models.TextField(null=False)

    def __str__(self):
        return self.title