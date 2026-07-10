from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils import timezone

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from patients.models import Patient
from doctors.models import Doctor


class DashboardView(APIView):

    def get(self, request):

        today = timezone.now().date()


        total_patients = Patient.objects.count()


        total_doctors = Doctor.objects.count()


        today_appointments = Appointment.objects.filter(
            appointment_date=today,
            status="Booked"
        ).count()


        upcoming_appointments = Appointment.objects.filter(
            appointment_date__gt=today,
            status="Booked"
        ).count()


        data = {

            "patients": total_patients,

            "doctors": total_doctors,

            "today_appointments": today_appointments,

            "upcoming_appointments": upcoming_appointments

        }


        return Response(data)
    
class GlobalSearchView(APIView):

    def get(self, request):

        query = request.GET.get("q")


        if not query:

            return Response(
                {
                    "message":"Please enter search value"
                },
                status=400
            )


        patients = Patient.objects.filter(
            full_name__icontains=query
        )


        doctors = Doctor.objects.filter(
            doctor_name__icontains=query
        )


        patient_data = []


        for patient in patients:

            patient_data.append({

                "id": patient.id,

                "patient_id":
                patient.patient_id,

                "full_name":
                patient.full_name,

                "email":
                patient.email

            })



        doctor_data = []


        for doctor in doctors:

            doctor_data.append({

                "id": doctor.id,

                "doctor_name":
                doctor.doctor_name,

                "department":
                doctor.department

            })


        response = {

            "patients":
            patient_data,


            "doctors":
            doctor_data

        }


        return Response(response)