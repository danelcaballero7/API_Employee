from django.urls import path, include
from EmployeeApp import views
from django.conf.urls.static import static
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'bosses', views.BossesViewSet)
router.register(r'departments', views.DepartmentsViewSet)
router.register(r'employees', views.EmployeesViewSet)

urlpatterns= [
    path('', include(router.urls))
]
