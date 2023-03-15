from django import forms
from django.db.models.base import Model
from django .forms import fields
from .models import Employee


class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"