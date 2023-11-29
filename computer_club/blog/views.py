from django.shortcuts import render, redirect
from blog.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
import datetime


from django.shortcuts import  render, redirect

 #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

# Create your views here.
@csrf_exempt
def reg(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful." )
            return render(request, 'blog/base.html', {user : user})
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render (request=request, template_name="blog/reg.html", context={"register_form":form})
# @login_required
def ini(request, user = None):
    return render(request, 'Techie/index.html', {"user" : user})

users = []

def login_request(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('name')
            password = form.cleaned_data.get('passw')
            try:
                user = User.objects.get(name=username,passw = password)
                users.append(user)
            except:
                user = None
            # user = authenticate(name=username, passw=password)
            # print(username,password)
            if user is not None:
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, 'Techie/index.html', {'user' : user})
            else:
                print("nope")
                messages.error(request,"Invalid username or password.")
        else:
            print("not")
            messages.error(request,"Invalid username or password.")
            
    form = LoginForm()
    return render(request=request, template_name="Techie/login.html", context={"login_form":form})


def del_order(request):
    
    user = User.objects.filter(id=users[-1].id)
    print(user)
    order = OrderTable.objects.filter(id = user[0].order.id)
    user.update(order=None)
    order.delete()
    user = User.objects.filter(id=users[-1].id)
    users[-1] = user[0]
    return render(request, 'Techie/index.html',{'user':users[-1]}) 

def add_order(request):
    print("its")

    if request.method == "POST":
        form = OrderCreationForm(request.POST)
        print(request.POST)
        print(form.errors)
        
        if form.is_valid():
            
            print("saved")
            order = form.save()
            user = User.objects.filter(id=users[-1].id).update(order=order)
            user = User.objects.filter(id=users[-1].id)
            users[-1] = user[0]
            
            
            # messages.success(request, "Registration successful." )
            return render(request, 'Techie/index.html',{'user':users[-1]})
        print("not_valid")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    print(request.user)
    
    form = OrderCreationForm()
    # 
    return render(request, 'Techie/add_order.html', {"form" : form,'user':users[-1]})

def load_cities(request):
    print("tuta")
    computer_id = request.GET.get('comp_club_id')

    computers = Computer.objects.filter(computer_club=computer_id).all()
    return render(request, 'Techie/comp_dropdown_list_options.html', {'attrs': computers})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def load_times(request):
    print("tuta2")
    comp_id = request.GET.get('comp_id')
    times = OrderTable.objects.filter(computer = comp_id)
    current_orders = []
    for i in range(len(times)):
        if times[i].date_start.date() == datetime.date.today():
            current_orders.append(datetime.datetime.combine(datetime.date.today(),times[i].date_start.time()))
    time = []
    print(current_orders)
    now = datetime.datetime.now()
    # dd/mm/YY H:M:S
    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    for i in range(len(t)):
        h,m,s = t[i][1].split(":")
        if not datetime.datetime.combine(datetime.date.today(),datetime.time(hour=int(h),minute=int(m),second=int(s))) in current_orders and datetime.datetime.combine(datetime.date.today(),datetime.time(hour=int(h),minute=int(m),second=int(s))) > now:
            date = datetime.datetime.combine(datetime.date.today(),datetime.time(hour=int(h),minute=int(m),second=int(s)))
            true_date =  str(date.date()) + t[i][0][10::]
            time.append((true_date,date))
    return render(request, 'Techie/time_dropdown_list_options.html', {'attrs': time})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def load_form(request):
    print("tuta_from")
    date_start = request.GET.get('time')
    print(date_start)
    # computers = Computer.objects.filter(computer_club=computer_id).all()
    return render(request, 'Techie/time_dropdown_list_options.html', {'attrs': date_start})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

t = [
    ("2022-11-15 00:00:00.000000-00:00",'00:00:00'),
    ("2022-11-15 01:00:00.000000-00:00",'01:00:00'),
    ("2022-11-15 02:00:00.000000-00:00",'02:00:00'),
    ("2022-11-15 03:00:00.000000-00:00",'03:00:00'),
    ("2022-11-15 04:00:00.000000-00:00",'04:00:00'),
    ("2022-11-15 05:00:00.000000-00:00",'05:00:00'),
    ("2022-11-15 06:00:00.000000-00:00",'06:00:00'),
    ("2022-11-15 07:00:00.000000-00:00",'07:00:00'),
    ("2022-11-15 08:00:00.000000-00:00",'08:00:00'),
    ("2022-11-15 09:00:00.000000-00:00",'09:00:00'),
    ("2022-11-15 10:00:00.000000-00:00",'10:00:00'),
    ("2022-11-15 11:00:00.000000-00:00",'11:00:00'),
    ("2022-11-15 12:00:00.000000-00:00",'12:00:00'),
    ("2022-11-15 13:00:00.000000-00:00",'13:00:00'),
    ("2022-11-15 14:00:00.000000-00:00",'14:00:00'),
    ("2022-11-15 15:00:00.000000-00:00",'15:00:00'),
    ("2022-11-15 16:00:00.000000-00:00",'16:00:00'),
    ("2022-11-15 17:00:00.000000-00:00",'17:00:00'),
    ("2022-11-15 18:00:00.000000-00:00",'18:00:00'),
    ("2022-11-15 19:00:00.000000-00:00",'19:00:00'),
    ("2022-11-15 20:00:00.000000-00:00",'20:00:00'),
    ("2022-11-15 21:00:00.000000-00:00",'21:00:00'),
    ("2022-11-15 22:00:00.000000-00:00",'22:00:00'),
    ("2022-11-15 23:00:00.000000-00:00",'23:00:00'),
]

times1 = [
    ('1',"2022-11-15 04:00:00.000000-00:00"),
    ('2',datetime.time(hour=1,minute=0,second=0)),
    ('3',datetime.time(hour=2,minute=0,second=0)),
    ('4',datetime.time(hour=3,minute=0,second=0)),
    ('5',datetime.time(hour=4,minute=0,second=0)),
    ('6',datetime.time(hour=5,minute=0,second=0)),
    ('7',datetime.time(hour=6,minute=0,second=0)),
    ('8',datetime.time(hour=7,minute=0,second=0)),
    ('9',datetime.time(hour=8,minute=0,second=0)),
    ('10',datetime.time(hour=9,minute=0,second=0)),
    ('11',datetime.time(hour=10,minute=0,second=0)),
    ('12',datetime.time(hour=11,minute=0,second=0)),
    ('13',datetime.time(hour=12,minute=0,second=0)),
    ('14',datetime.time(hour=13,minute=0,second=0)),
    ('15',datetime.time(hour=14,minute=0,second=0)),
    ('16',datetime.time(hour=15,minute=0,second=0)),
    ('17',datetime.time(hour=16,minute=0,second=0)),
    ('18',datetime.time(hour=17,minute=0,second=0)),
    ('19',datetime.time(hour=18,minute=0,second=0)),
    ('20',datetime.time(hour=19,minute=0,second=0)),
    ('21',datetime.time(hour=20,minute=0,second=0)),
    ('22',datetime.time(hour=21,minute=0,second=0)),
    ('23',datetime.time(hour=22,minute=0,second=0)),
    ('24',datetime.time(hour=23,minute=0,second=0)),
]