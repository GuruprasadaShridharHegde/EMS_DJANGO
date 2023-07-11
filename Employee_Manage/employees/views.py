from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.
def home(request):
    employees = Employee.objects.all
    return render(request,"employees/home.html",{'employees':employees})

def add_employees(request):
    if request.method == "POST":
        print("Field Added")
        print("fdds",request.POST)
        # To retrieve user inputs
        employee_id = request.POST.get("employee_id")
        employee_name = request.POST.get("employee_name")
        employee_email = request.POST.get("employee_email")
        employee_address = request.POST.get("employee_address")
        employee_phone = request.POST.get("employee_phone")


        # cretae an objects for models
        s = Employee()
        s.Employee_ID = employee_id
        s.Name = employee_name
        s.Email = employee_email
        s.Address = employee_address
        s.Phone_No = employee_phone

        s.save()
        return redirect("/employees/home")
    return render(request,"employees/add_employees.html",{})

def delete_employees(request,Employee_ID):
    s= Employee.objects.get(pk=Employee_ID)
    s.delete()

    return redirect("/employees/home")
def update_employees(request,Employee_ID):
    employees=Employee.objects.get(pk=Employee_ID)
    print("ok2",employees)
    return render(request,"employees/update_employees.html",{'employees':employees})

def do_update_employees(request, Employee_ID):
    employee_id = request.POST.get("employee_id")
    employee_name = request.POST.get("employee_name")
    employee_email = request.POST.get("employee_email")
    employee_address = request.POST.get("employee_address")
    employee_phone = request.POST.get("employee_phone")

    employee = Employee.objects.get(pk=Employee_ID)

    employee.Employee_ID = employee_id
    employee.Name = employee_name
    employee.Email = employee_email
    employee.Address = employee_address
    employee.Phone_No = employee_phone

    employee.save()

    return redirect("/employees/home")
