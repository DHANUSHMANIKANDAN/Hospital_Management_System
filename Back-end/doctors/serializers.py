from rest_framework import serializers
from .models import Doctor
import re


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Doctor

        fields = [
            "id",
            "doctor_name",
            "department",
            "qualification",
            "experience",
            "consultation_fee",
            "mobile_number",
            "created_at"
        ]

        read_only_fields = [
            "id",
            "created_at"
        ]


    def validate_mobile_number(self, value):

        if not re.match(r'^[0-9]{10}$', value):

            raise serializers.ValidationError(
                "Mobile number must contain 10 digits"
            )

        return value


    def validate_experience(self, value):

        if value < 0:

            raise serializers.ValidationError(
                "Experience cannot be negative"
            )

        return value


    def validate_consultation_fee(self,value):

        if value <= 0:

            raise serializers.ValidationError(
                "Consultation fee must be greater than zero"
            )

        return value