from django.urls import path
from .views import *
from django.urls import reverse
from .views import register_employee, employee_list, update_employee

app_name = "employee"

urlpatterns = [
    path("register/", register_employee, name="Employee-registartion"),
    path("view/", employee_list, name="employee_list"),
    path("update/", update_employee, name = "update Employee")



]