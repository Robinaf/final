# from email import message
# from pyexpat import model
# from turtle import title
# from unittest.util import _MAX_LENGTH
from django.db import models
from users.models import Customer

# Create your models here.
class WaterCustomer(models.Model):
    meter_id=models.IntegerField(primary_key=True)
    username = models.ForeignKey(null=False,max_length=100, on_delete=models.CASCADE, to = Customer)
    class Meta:
        db_table = "water_customer"

    # def __str__(self):
    #     return self.title
class WaterBillInfo(models.Model):
    meter_id=models.ForeignKey(on_delete=models.CASCADE, to=WaterCustomer)
    prev_reading = models.DecimalField(max_digits=50,decimal_places=2)
    current_reading = models.DecimalField(max_digits=50,decimal_places=2)
    date =models.DateField(null=True)
    status = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "waterbillinfo"

class WaterComplain(models.Model):
    meter_id = models.ForeignKey(on_delete=models.CASCADE, to=WaterCustomer)
    complain = models.TextField()
    date = models.DateField(null=True)
    status = models.CharField(max_length=50,null=True)
    class Meta:
        db_table = "water_complain"
