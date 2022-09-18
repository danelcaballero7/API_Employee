from django.db import models

# Create your models here.
class Departments(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

    def __str__(self):
        return self.DepartmentName

class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.ImageField(upload_to="blog", null=True, blank=True )
    DepartmentID = models.ForeignKey(Departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.EmployeeName

class Bosses(models.Model):
    BossesName= models.CharField(max_length=100)
    BossesLast_name = models.CharField(max_length=100)
    BossesAge = models.IntegerField()
    DepartmentID = models.OneToOneField(Departments, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.BossesName
