from django.urls import path
from .views import ListEmployeesView

urlpatterns = [
    path('employees/',ListEmployeesView.as_view(),name="employees-all")
]
