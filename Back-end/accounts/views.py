from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import LoginSerializer


class LoginView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            try:
                user = User.objects.get(email=email)

            except User.DoesNotExist:
                return Response(
                    {"message": "Invalid Email"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user = authenticate(
                username=user.username,
                password=password
            )

            if user:

                refresh = RefreshToken.for_user(user)

                return Response({
                    "message": "Login Successful",

                    "access": str(refresh.access_token),

                    "refresh": str(refresh),

                    "username": user.username,

                    "email": user.email

                })

            return Response(
                {"message": "Invalid Password"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(serializer.errors)