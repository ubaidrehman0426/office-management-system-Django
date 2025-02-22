from django.shortcuts import render,HttpResponse
from .models import Employee,Role,department
import datetime

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps': emps
    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=='POST':
        try:
            first_name=request.POST['First_name']
            last_name=request.POST['Last_name']
            salary=int(request.POST['salary'])
            dept=request.POST['dept']
            bonus=int(request.POST['bonus'])
            phone=request.POST['phone']
            role=request.POST['role']
            
            dept_obj = department.objects.get(name=dept)
            role_obj = Role.objects.get(name=role)
            
            new_emp = Employee(
                First_name=first_name,
                Last_name=last_name,
                salary=salary,
                bonus=bonus,
                phone=phone,
                dept=dept_obj,
                role=role_obj,
                hire_date=datetime.date.today()
            )
            new_emp.save()
            return HttpResponse('Employee added Successfully')
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")
    elif request.method=='GET':
        departments = department.objects.all()
        roles = Role.objects.all()
        context = {
            'departments': departments,
            'roles': roles
        }
        return render(request,'add_emp.html', context)
    else:
        return HttpResponse("An Exception Occurred! Employee has not been added")



def remove_emp(request):
    if request.method == 'POST':
        try:
            emp_id = request.POST.get('emp_id')
            emp = Employee.objects.get(id=emp_id)
            emp.delete()
            return HttpResponse('Employee Removed Successfully')
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'remove_emp.html', context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dept = request.POST.get('dept')
        role = request.POST.get('role')
        
        emps = Employee.objects.all()
        
        if name:
            emps = emps.filter(First_name__icontains=name) | emps.filter(Last_name__icontains=name)
        if dept:
            emps = emps.filter(dept__name__icontains=dept)
        if role:
            emps = emps.filter(role__name__icontains=role)
            
        context = {
            'emps': emps,
            'departments': department.objects.all(),
            'roles': Role.objects.all()
        }
        return render(request, 'filter_emp.html', context)
    
    context = {
        'departments': department.objects.all(),
        'roles': Role.objects.all()
    }
    return render(request, 'filter_emp.html', context)
