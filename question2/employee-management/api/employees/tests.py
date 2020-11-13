from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from . models import Employees
from .serializers import EmployeesSerializer
# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    def add_employee(id=0, firstname="", managername=""):
        if firstname !="" and lastname !="":
            Employees.objects.create(id=id, firstname=firstname, managername=managername)

    def setUp(self):
        self.add_employee(1, "A", "M")
        self.add_employee(2, "B", "M")
        self.add_employee(3, "C", "M")

class GetAllEmployeesTest(BaseViewTest):

    def test_get_all_employees(self):
        response = self.client.get(
            reverse("employees-all",kwargs={"version":"v1"})
        )

        expected = Employees.objects.all()
        serialized = EmployeesSerializer(expected, many=True)
        self.assertEqual(response.data,serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
