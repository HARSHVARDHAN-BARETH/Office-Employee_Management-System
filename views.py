from django.shortcuts import render, HttpResponse
from .models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def viewEmp(request):
    emp = Employee.objects.all()
    context = {
        'emp':emp
    }
    print(context)
    return render(request, 'viewEmp.html', context)

def AddEmp(request):
   if request.method == "POST":
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       salary = int(request.POST['salary'])
       bonus = int(request.POST['bonus'])
       phone = int(request.POST['phone'])
       dept = int(request.POST['dept'])  # Corrected variable name for department
       role = int(request.POST['role'])  # Corrected variable name for role
       new = Employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone, dept_id=dept, role_id=role, hireDate=datetime.now())
       new.save()
       return HttpResponse("Employee Added Successfully!")
   elif request.method=="GET":
        return render(request, 'AddEmp.html')
   else:
         return HttpResponse("An Exception Occured! Employee Has not been Added")
    
def RemoveEmp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee Removed Successfully!")
        except:
            return HttpResponse("Please, Enter a valid Employee Id")
    emp = Employee.objects.all()
    context = {
        'emp':emp 
    }
    
    return render(request, 'RemoveEmp.html', context)

def FillterApp(request):
    if request.method == "POST":
        name = request.POST['name'],
        dept = request.POST['dept'],
        role = request.POST['role'],
        emp = Employee.objects.all()
        if name:
            emp = emp.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            emp = emp.filter(dept__name = dept)
        if role:
            emp = emp.filter(role__name = role)
        
        context = {
            'emp' : emp
        }
        
        return render(request, "viewEmp.html", context)
    elif request.method == "GET":
        return render(request, 'FillterApp.html')
    else:
        return HttpResponse("An Exception Occured!")