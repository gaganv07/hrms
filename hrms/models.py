from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Employee(models.Model):
    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("ON_LEAVE", "On leave"),
        ("INACTIVE", "Inactive"),
    ]
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80, blank=True)
    email = models.EmailField(unique=True)
    job_title = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="employees")
    date_joined = models.DateField()
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="ACTIVE")

    class Meta:
        ordering = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()
