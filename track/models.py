from django.db import models

class Track(models.Model):
    waybill=models.CharField(max_length=20,primary_key=True)
    pickup=models.DateField()
    origin=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)

    CHOICES = [
    ('Open For Pickup', 'Open For Pickup'),
    ('In Transit', 'In Transit'),
    ('Delivered', 'Delivered'),
    ('Returned', 'Returned'),
    ]

    status=models.CharField(choices=CHOICES, max_length=50)
    EDD=models.DateField()
    phone=models.CharField(max_length=15)
    receiver=models.CharField(max_length=50)
    lastscan=models.CharField(max_length=50)



class Lead(models.Model): 
    type=models.CharField(max_length=50)
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    address1=models.CharField(max_length=100)
    address2=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pin=models.CharField(max_length=10)
    country=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    feedback=models.TextField(max_length=150)


