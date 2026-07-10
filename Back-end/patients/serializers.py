from rest_framework import serializers
from datetime import date
from .models import Patient
import re


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = [
            "id",
            "patient_id",
            "full_name",
            "gender",
            "dob",
            "phone_number",
            "email",
            "blood_group",
            "address",
            "created_at"
        ]

        read_only_fields = [
            "id",
            "patient_id",
            "created_at"
        ]
        
    def validate_dob(self, value):

        if value > date.today():
            raise serializers.ValidationError(
                "Date of birth cannot be in the future"
            )

        return value


    def validate_phone_number(self, value):

        pattern = r'^[0-9]{10}$'

        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Phone number must contain 10 digits"
            )

        return value


    def validate_email(self, value):

        if Patient.objects.filter(email=value).exists():

            raise serializers.ValidationError(
                "Email already exists"
            )

        return value