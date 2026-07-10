from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Appointment
from .serializers import AppointmentSerializer



class AppointmentListCreateView(APIView):


    def get(self, request):

        appointments = Appointment.objects.all()


        serializer = AppointmentSerializer(
            appointments,
            many=True
        )


        return Response(
            serializer.data
        )



    def post(self, request):

        serializer = AppointmentSerializer(
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




class AppointmentDetailView(APIView):


    def get_object(self,id):

        try:

            return Appointment.objects.get(id=id)

        except Appointment.DoesNotExist:

            return None



    def get(self,request,id):

        appointment = self.get_object(id)


        if not appointment:

            return Response(
                {
                    "message":"Appointment not found"
                },
                status=404
            )


        serializer = AppointmentSerializer(
            appointment
        )


        return Response(
            serializer.data
        )



    def put(self,request,id):

        appointment = self.get_object(id)


        if not appointment:

            return Response(
                {
                    "message":"Appointment not found"
                },
                status=404
            )


        serializer = AppointmentSerializer(
            appointment,
            data=request.data
        )


        if serializer.is_valid():

            serializer.save()


            return Response(
                serializer.data
            )


        return Response(
            serializer.errors,
            status=400
        )



    def delete(self,request,id):

        appointment = self.get_object(id)


        if not appointment:

            return Response(
                {
                    "message":"Appointment not found"
                },
                status=404
            )


        appointment.delete()


        return Response(
            {
                "message":
                "Appointment deleted successfully"
            }
        )
        
    def patch(self,request,id):

            appointment = self.get_object(id)


            if not appointment:

                return Response(
                    {
                        "message":"Appointment not found"
                    },
                    status=404
                )


            appointment.status = "Cancelled"

            appointment.save()


            return Response(
                    {
                        "message":
                        "Appointment cancelled successfully"
                    }
                )