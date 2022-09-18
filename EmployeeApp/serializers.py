from rest_framework import serializers
from EmployeeApp.models import Departments, Employees, Bosses


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentName',)


class EmployeesSerializer(serializers.ModelSerializer):
    # department = DepartmentsSerializer(source='Department')
    class Meta:
        model = Employees
        fields = ('EmployeeName', 'DepartmentID', 'DateOfJoining', 'PhotoFileName', 'DepartmentID')

class BossesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bosses
        fields = ('BossesName', 'BossesLast_name', 'BossesAge', 'DepartmentID')
