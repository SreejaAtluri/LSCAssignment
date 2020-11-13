from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Employees
from .serializers import EmployeesSerializer

class ListEmployeesView(generics.ListAPIView):

    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
