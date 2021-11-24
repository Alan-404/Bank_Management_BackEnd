from django.conf.urls import url
from employee import views

urlpatterns= [
    url(r"^employee_api", views.employeeApi),
    url(r"^token$", views.getNameByToken)
]