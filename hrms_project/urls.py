
from django.contrib import admin
from django.urls import path
from hrms import views

urlpatterns = [
    path("admin/", admin.site.urls),

    
    path("", views.dashboard, name="dashboard"),

    
    path("employees/", views.employee_list, name="employee_list"),

    
    path(
        "employees/add/",
        views.employee_create,
        name="employee_create",
    ),
    path(
        "employees/<int:pk>/edit/",
        views.employee_update,
        name="employee_update",
    ),
    path(
        "employees/<int:pk>/delete/",
        views.employee_delete,
        name="employee_delete",
    ),
]
