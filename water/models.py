# from email import message
# from pyexpat import model
# from turtle import title
# from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime, timedelta
from users.models import Customer
from users.models import *
from django.utils import timezone
from django.contrib.auth.models import UserManager
# Create your models here.
class WaterCustomer(models.Model):
    meter_id=models.IntegerField(primary_key=True)
    username = models.OneToOneField(Customer,null=False,max_length=100, on_delete=models.CASCADE, )
    
    objects = CustomAccountManager()
    
    class Meta:
        db_table = "water_customer"
    def __str__(self):
        return str(self.meter_id )
    def __unicode__(self):
        return self.meter_id

    # def __str__(self):
    #     return self.title
class WaterTechnician(Account):
    employee_id = models.IntegerField(null=True)
    # username=models.OneToOneField(Account,null=False,max_length=100,on_delete=models.CASCADE)
    class Meta:
        db_table = "water_technician"
    def __str__(self):
        return str(self.username)
class WaterReader(Account):
    employee_id=models.IntegerField(null=True)
    # username=models.OneToOneField(Account,null=False,max_length=100,on_delete=models.CASCADE)
    class Meta:
        db_table ="water_reader"
    def __str__(self):
        return str(self.username)
class WaterBillInfo(models.Model):
    meter_id=models.ForeignKey(on_delete=models.CASCADE, to=WaterCustomer)
    prev_reading = models.DecimalField(max_digits=50,decimal_places=2,default=0)
    current_reading = models.DecimalField(max_digits=50,decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
    is_paid = models.BooleanField(max_length=50,default=False)
    # Month_choice = [('january','january'),('february','february'),('march','march'),('april','april'),
    # ('may','may'),('june','june'),('july','july'),('august','august'),('september','september'),('october','october'),('november','november'),('december','december')]
    # month=models.CharField(max_length=50,choices=Month_choice,blank=True,null = True)
    # year = models.IntegerField(null=True)
    amount = models.DecimalField(max_digits=50,decimal_places=2,null=True)
    deadline =models.DateTimeField(default=datetime.now() + timedelta(days=3))
    class Meta:
        db_table = "waterbillinfo"
    def __str__(self):
        return str(self.meter_id)


class WaterComplain(models.Model):
    id =models.AutoField(primary_key=True)
    meter_id = models.ForeignKey(on_delete=models.CASCADE, to=WaterCustomer)
    complain = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    is_solved = models.CharField(max_length=50,default=False )#null=True,default='not solved')
    phone_number=models.IntegerField(null=True)
    assigned_to=models.ForeignKey(WaterTechnician,null=True,max_length=100, on_delete=models.CASCADE,)
    tec_reported=models.BooleanField(max_length=50,default=False )
    
    class Meta:
        db_table = "water_complain"
    def __str__(self):
        return str(self.id)
    def __unicode__(self):
        return self.meter_id
class AssignComplain(models.Model):
    complain_id=models.ForeignKey(on_delete = models.CASCADE , to=WaterComplain)
    assign_to =models.ForeignKey(on_delete=models.CASCADE, to =WaterTechnician)
    def __str__(self):
        return str(self.assign_to)

    # def save(self, *args, **kwargs):
    #     meter_id = self.request.user.meter_id
    #     print("-"*50)
    #     print(meter_id)
    #     print("-"*50)

class WaterBalance(models.Model):
    balance = models.DecimalField(max_digits=50,default=0.00,decimal_places=2)
    def __str__(self):
        return str(self.balance)
