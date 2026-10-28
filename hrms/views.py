from django.shortcuts import render
from django.db.models import Q
from .models import Department, Employee

def dashboard(request):
    departments = Department.objects.all()
    context = {
        "employee_count": Employee.objects.count(),
        "department_count": departments.count(),
        "active_count": Employee.objects.filter(status="ACTIVE").count(),
        "on_leave_count": Employee.objects.filter(status="ON_LEAVE").count(),
        "departments": departments,
        "recent_employees": Employee.objects.select_related("department").order_by("-date_joined")[:5],
    }
    return render(request, "hrms/dashboard.html", context)

def employee_list(request):
    query = request.GET.get("q", "").strip()
    employees = Employee.objects.select_related("department")
    if query:
        employees = employees.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) |
            Q(employee_id__icontains=query) | Q(email__icontains=query) |
            Q(department__name__icontains=query)
        )
    return render(request, "hrms/employees.html", {"employees": employees, "query": query})

from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee


def employee_create(request):
    form = EmployeeForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("employee_list")

    return render(
        request,
        "hrms/employee_form.html",
        {"form": form, "page_title": "Add Employee"},
    )


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("employee_list")

    return render(
        request,
        "hrms/employee_form.html",
        {"form": form, "page_title": "Edit Employee"},
    )


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        employee.delete()
        return redirect("employee_list")

    return render(
        request,
        "hrms/employee_confirm_delete.html",
        {"employee": employee},
    )
