from django.urls import path

from .views import (
    DoctorListCreateView,
    DoctorDetailView
)


urlpatterns = [

    path(
        "",
        DoctorListCreateView.as_view()
    ),


    path(
        "<int:id>/",
        DoctorDetailView.as_view()
    )

]