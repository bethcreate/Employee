from django.shortcuts import render, redirect
from .forms import EmployeeRegistrationForm
from .models import Employee
from . import views


def register_employee(request):
    if request.method=="POST":
        form = EmployeeRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)

    else:
        form=EmployeeRegistrationForm()
    return render(request,"register_employee.html",{"form":form,})


def employee_list(request):
    employees= Employee.objects.all()
    return render(request, "employee_list.html", {"employees":employees})

def update_employee(request, id):
    employee=Employee.objects.get(id=id)

    if request.method == "POST":
        form = EmployeeRegistrationForm(request.post,instance=employee)
        if form.is_valid():
            form.save()
        return redirect("view_employee", id=employee.id, )

    else:
        form=EmployeeRegistrationForm(instance=employee)

        return render(request,"update_employee.html", {"form": form})
