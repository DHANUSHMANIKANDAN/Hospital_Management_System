from django.urls import path

from .views import (
    DashboardView,
    GlobalSearchView
)


urlpatterns = [

    path(
        "",
        DashboardView.as_view()
    ),


    path(
        "search/",
        GlobalSearchView.as_view()
    )

]