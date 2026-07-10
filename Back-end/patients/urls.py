from django.urls import path

from .views import (
    PatientListCreateView,
    PatientDetailView,
    PatientProfileView
)


urlpatterns = [

    path(
        "",
        PatientListCreateView.as_view()
    ),


    path(
        "<int:id>/",
        PatientDetailView.as_view()
    ),


    path(
        "<int:id>/profile/",
        PatientProfileView.as_view()
    )

]