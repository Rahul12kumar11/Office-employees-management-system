from django.shortcuts import render, HttpResponse, redirect
from .models import Employees,role,Department, Contact
from datetime import datetime
from django.db.models import Q
from .forms import DepartmentForm, roleForm
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
# Create your views here.

def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employees.objects.all()
    context = {
        'emps' : emps
    }
    return render(request,'all_emp.html',context)
    

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dept = int(request.POST['dept'])
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        role = int(request.POST['role'])
        phone = int(request.POST['phone'])
        
        new_emp = Employees(first_name=first_name, last_name=last_name, dept_id=dept, salary=salary, bonus=bonus, role_id=role, phone=phone, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('Employee added Succesfully')

    elif request.method == 'GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse('An error is found')


    return render(request,'add_emp.html')
def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_remove = Employees.objects.get(id=emp_id)
            emp_to_remove.delete()
            return HttpResponse("Employee remove succesfully")
        
        except:
            return HttpResponse("Please enter a valid employee id")

    emps = Employees.objects.all()
    context = {
        'emps' : emps
    }
    return render(request,'remove_emp.html', context)
def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employees.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        
        if dept:
            emps = emps.filter(dept__name = dept)

        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps' : emps
        }
        return render(request, 'all_emp.html', context)
    
    elif request.method == 'GET':
        return render(request,'filter_emp.html')

    else:
        return HttpResponse('An error occur')

def about(request):
    return render(request, 'about.html')

def home(request):
    return redirect('/index')

def contact(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        country = request.POST['country']
        subject = request.POST['subject']
        
        new_cnt = Contact(firstname=firstname, lastname=lastname, phone=phone, country=country, subject=subject)
        new_cnt.save()
        return HttpResponse('Employee added Succesfully')

    elif request.method == 'GET':
        return render(request,'contact.html')
    else:
        return HttpResponse('An error is found')

def dep(request):
    if request.method == "POST":
        dep = DepartmentForm(request.POST)
        if dep.is_valid():
            dep.save()
            return HttpResponse("Department added sucessfully")
    elif request.method == 'GET':
        dep = DepartmentForm()
        return render(request, 'dep.html', {'form':dep})
    else:
        return HttpResponse('An error detected')

def role(request):
    if request.method == "POST":
        rol = roleForm(request.POST)
        if rol.is_valid():
            rol.save()
            return HttpResponse("Department added sucessfully")
    elif request.method == 'GET':
        rol = roleForm()
        return render(request, 'role.html', {'form':rol})
    else:
        return HttpResponse('An error detected')