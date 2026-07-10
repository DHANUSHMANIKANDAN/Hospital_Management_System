from django.db import models

# Create your models here.
from django.db import models


class Doctor(models.Model):

    DEPARTMENTS = [

        ("Cardiology", "Cardiology"),

        ("Orthopaedics", "Orthopaedics"),

        ("Neurology", "Neurology"),

        ("General Medicine", "General Medicine"),

        ("Pediatrics", "Pediatrics"),

    ]

    doctor_name = models.CharField(max_length=100)

    department = models.CharField(
        max_length=50,
        choices=DEPARTMENTS
    )

    qualification = models.CharField(max_length=100)

    experience = models.PositiveIntegerField()

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    mobile_number = models.CharField(max_length=15)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doctor_name