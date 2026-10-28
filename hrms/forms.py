
from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "employee_id",
            "first_name",
            "last_name",
            "email",
            "job_title",
            "department",
            "date_joined",
            "status",
        ]

        widgets = {
            "date_joined": forms.DateInput(
                attrs={"type": "date"}
            ),
        }
