from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Doctor
from .serializers import DoctorSerializer



class DoctorListCreateView(APIView):


    def get(self, request):

        search = request.GET.get("search")


        doctors = Doctor.objects.all()


        if search:

            doctors = doctors.filter(
                doctor_name__icontains=search
            )


        serializer = DoctorSerializer(
            doctors,
            many=True
        )


        return Response(serializer.data)



    def post(self, request):

        serializer = DoctorSerializer(
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



class DoctorDetailView(APIView):


    def get_object(self,id):

        try:

            return Doctor.objects.get(id=id)

        except Doctor.DoesNotExist:

            return None



    def get(self,request,id):

        doctor = self.get_object(id)


        if not doctor:

            return Response(
                {
                    "message":"Doctor not found"
                },
                status=404
            )


        serializer = DoctorSerializer(doctor)

        return Response(serializer.data)



    def put(self,request,id):

        doctor = self.get_object(id)


        if not doctor:

            return Response(
                {
                    "message":"Doctor not found"
                },
                status=404
            )


        serializer = DoctorSerializer(
            doctor,
            data=request.data
        )


        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)


        return Response(
            serializer.errors,
            status=400
        )



    def delete(self,request,id):

        doctor = self.get_object(id)


        if not doctor:

            return Response(
                {
                    "message":"Doctor not found"
                },
                status=404
            )


        doctor.delete()


        return Response(
            {
                "message":"Doctor deleted successfully"
            }
        )