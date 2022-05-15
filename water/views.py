from multiprocessing import context
from django.db.models import IntegerField
from django.db.models.functions import Cast
from django.shortcuts import render,redirect
from .models import WaterBillInfo,WaterCustomer,WaterComplain
from django.http import HttpResponse
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.decorators import login_required


# Create your views here.
def water_admin(request):
    wc=WaterCustomer.objects.all()

    return render(request,'water_admin/index.html',{'WaterCustomer':wc})
def water_reader(request):

    if request.method=="POST":
        
        meter_id_id =request.POST.get('meter_id_id')
        
        current_reading = float(request.POST.get('current_reading'))
       
        # ww=bb.meter_id
        # x=request.user.username
        # y=WaterCustomer.objects.get(username=x)
        # m=y.meter_id
        
        month = request.POST.get('month')
        year = request.POST.get('year')
        # bb=WaterBillInfo.objects.get(meter_id_id=meter_id_id)
        # prev =bb.prev_reading
        wc = WaterCustomer.objects.get(meter_id=meter_id_id)
        try:
            prev_read = float(WaterBillInfo.objects.filter(meter_id=meter_id_id).order_by('-date')[0].current_reading)
        except:
            prev_read = 0
        ################################################
         # when reading is less than 50
        #################################################
        if current_reading-prev_read <= 50:
            print('is less tan 50')

            new_bill = WaterBillInfo.objects.create(
                meter_id_id = wc.meter_id,
                current_reading=float(current_reading), 
                amount=(current_reading-prev_read)*2, 
                prev_reading=prev_read,
                month=month,
                year=year,

            )
         ################################################
         # when reading is less than 100
        #################################################
        elif current_reading-prev_read <= 100:
            print('is less tan 100')
            new_bill = WaterBillInfo.objects.create(
                meter_id_id = wc.meter_id,
                current_reading=float(current_reading), 
                amount=(current_reading-prev_read)*3, 
                prev_reading=prev_read,
                month=month,
                year=year,

            )
        else:
            print(current_reading)
            print(prev_read)
            pass
        
        # prev_reading=float(prev)
        # # bi= WaterBillInfo.objects.filter(prev_reading=prev_reading)
        # # prev_reading=bi.prev_reading
        # current_reading=float(current_reading)
        # # if current_reading<=100:
            

        # billinfo = WaterBillInfo(
        #     meter_id_id = wc.meter_id,
           
             
        #     current_reading=float(current_reading),
        #     month=month,
        #     year=year,

        #     # prev_reading = wc.prev_reading,
            
        #     amount = (current_reading-prev_reading) *2

               
           

        # )
        # billinfo.save()
       
       
        return redirect ('water_reader')
    
    return render(request,'water_reader/water_reader.html')
# def admin_cheek_bill(request):
#     a=WaterBillInfo.objects.all()
 
#     context ={
#         'a':a
#     }
#     return render(request,'water_admin/water_admin.html',context)

# def complain(request):
#     if request.method=="POST":
#         # meter_id = request.user.meter_id
#         print("-"*50)
#         print(request.user)
#         print(request.user.first_name)
#         print(request.user.meter_id)
#         # print(meter_id)
#         print("-"*50)
#         # complain =request.POST.get('complain')
#         # wc=WaterCustomer.objects.get(meter_id=meter_id)
#         # user=WaterCustomer.objects.all()
#         # # if request.user.meter_id==meter_id:
#         # complaindetail = WaterComplain(
#         #      meter_id_id =wc.meter_id,
#         #      complain=complain
#         #        )
#         # complaindetail.save()
#         # return render(request,'customer/main.html')
#         # # return HttpResponse('Invalid Credentials...!!!')        
#     return render(request,'customer/complain1.html')


def complain(request):
    if request.method=="POST":
        complain=request.POST.get('complain')
        x=request.user.username
        y=WaterCustomer.objects.get(username=x)
        m=y.meter_id
        complaindetail = WaterComplain(
        meter_id_id =m,
             complain=complain
         )
        complaindetail.save()
        return render(request,'customer/main.html')

        
    return render(request,'customer/complain1.html',)