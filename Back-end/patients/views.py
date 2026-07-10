from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination # for pagination
from django.utils import timezone

from appointments.models import Appointment
from django.db.models import Q

from .models import Patient
from .serializers import PatientSerializer

class PatientPagination(PageNumberPagination):

    page_size = 5


class PatientListCreateView(APIView):

    def get(self, request):

        search = request.GET.get("search")


        patients = Patient.objects.all()


        if search:

            patients = patients.filter(
                full_name__icontains=search
            )

        paginator = PatientPagination()

        result_page = paginator.paginate_queryset(
            patients,
            request
        )


        serializer = PatientSerializer(
            result_page,
            many=True
        )


        return paginator.get_paginated_response(
            serializer.data
        )



        return Response(serializer.data)



    def post(self, request):

        serializer = PatientSerializer(
            data=request.data
        )


        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )


        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )



class PatientDetailView(APIView):


    def get_object(self, id):

        try:
            return Patient.objects.get(id=id)

        except Patient.DoesNotExist:

            return None



    def get(self, request, id):

        patient = self.get_object(id)


        if not patient:

            return Response(
                {"message":"Patient not found"},
                status=404
            )


        serializer = PatientSerializer(patient)

        return Response(serializer.data)



    def put(self, request, id):

        patient = self.get_object(id)


        if not patient:

            return Response(
                {"message":"Patient not found"},
                status=404
            )


        serializer = PatientSerializer(
            patient,
            data=request.data
        )


        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)


        return Response(
            serializer.errors,
            status=400
        )



    def delete(self, request, id):

        patient = self.get_object(id)


        if not patient:

            return Response(
                {"message":"Patient not found"},
                status=404
            )


        patient.delete()


        return Response(
            {"message":"Patient deleted successfully"}
        )
        
class PatientProfileView(APIView):


    def get(self, request, id):

        try:

            patient = Patient.objects.get(id=id)

        except Patient.DoesNotExist:

            return Response(
                {
                    "message": "Patient not found"
                },
                status=404
            )


        # Patient Details

        patient_data = {

            "patient_id": patient.patient_id,

            "full_name": patient.full_name,

            "gender": patient.gender,

            "dob": patient.dob,

            "phone_number": patient.phone_number,

            "email": patient.email,

            "blood_group": patient.blood_group,

            "address": patient.address

        }


        # Appointment History

        appointments = Appointment.objects.filter(
            patient=patient
        ).order_by(
            "-appointment_date"
        )


        appointment_history = []


        for appointment in appointments:

            appointment_history.append({

                "doctor":
                appointment.doctor.doctor_name,

                "department":
                appointment.doctor.department,

                "date":
                appointment.appointment_date,

                "time":
                appointment.appointment_time,

                "reason":
                appointment.reason,

                "status":
                appointment.status

            })


        # Upcoming Appointment

        today = timezone.now().date()


        upcoming = Appointment.objects.filter(

            patient=patient,

            appointment_date__gte=today,

            status="Booked"

        ).order_by(
            "appointment_date"
        ).first()



        upcoming_data = None


        if upcoming:

            upcoming_data = {

                "doctor":
                upcoming.doctor.doctor_name,

                "date":
                upcoming.appointment_date,

                "time":
                upcoming.appointment_time

            }



        response = {


            "patient_details":
            patient_data,


            "appointment_history":
            appointment_history,


            "upcoming_appointment":
            upcoming_data

        }


        return Response(response)