from rest_framework import serializers
from datetime import date, datetime

from .models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment

        fields = [
            "id",
            "patient",
            "doctor",
            "appointment_date",
            "appointment_time",
            "reason",
            "status",
            "created_at"
        ]

        read_only_fields = [
            "id",
            "status",
            "created_at"
        ]


    def validate_appointment_date(self, value):

        if value < date.today():

            raise serializers.ValidationError(
                "Appointment date cannot be in the past"
            )

        return value



    def validate(self, data):

        doctor = data.get("doctor")

        appointment_date = data.get(
            "appointment_date"
        )

        appointment_time = data.get(
            "appointment_time"
        )


        existing_appointment = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time,
            status="Booked"
        )


        # For update operation
        if self.instance:

            existing_appointment = existing_appointment.exclude(
                id=self.instance.id
            )


        if existing_appointment.exists():

            raise serializers.ValidationError(
                "Doctor already has an appointment at this time"
            )


        return data