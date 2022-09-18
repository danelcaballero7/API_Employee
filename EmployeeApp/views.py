from rest_framework import viewsets
from EmployeeApp.models import Departments, Employees, Bosses
from EmployeeApp.serializers import EmployeesSerializer, DepartmentsSerializer, BossesSerializer


# Create your views here.

class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer

class BossesViewSet(viewsets.ModelViewSet):
    queryset = Bosses.objects.all()
    serializer_class = BossesSerializer
