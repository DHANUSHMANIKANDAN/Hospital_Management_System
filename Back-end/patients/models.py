from django.db import models

# Create your models here.
class Patient(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    BLOOD_GROUPS = [
        ("A+", "A+"),
        ("A-", "A-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"),
        ("AB-", "AB-"),
        ("O+", "O+"),
        ("O-", "O-"),
    ]

    patient_id = models.CharField(max_length=20, unique=True)

    full_name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    dob = models.DateField()

    phone_number = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    blood_group = models.CharField(
        max_length=5,
        choices=BLOOD_GROUPS
    )

    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
    
    def save(self, *args, **kwargs):

        if not self.patient_id:

            last_patient = Patient.objects.order_by("id").last()

            if last_patient:

                last_id = int(last_patient.patient_id[3:])

                self.patient_id = f"PAT{last_id+1:03d}"

            else:

                self.patient_id = "PAT001"

        super().save(*args, **kwargs)