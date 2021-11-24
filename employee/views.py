from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse 

from employee.models import EmployeeModel
from employee.serializer import EmployeeSerializer
from account.models import AccountModel

from common.lib import getIdByToken
# Create your views here.

@api_view(['GET', 'POST'])
def employeeApi(request):
    if request.method == "GET":
        try:
            employees = EmployeeModel.objects.all()
            employees_serializer = EmployeeSerializer(employees, many = True)
            return JsonResponse({"employees": employees_serializer.data})
        except Exception as e:
            return JsonResponse({"message": str(e)})
    elif request.method == "POST":
        try:
            employee_data = JSONParser().parse(request)
            employee_serializer = EmployeeSerializer(data=employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse({"success": True})
            return JsonResponse({"success": False})
        except Exception as e:
            return JsonResponse({"success": False})




@api_view(["GET"])
def getNameByToken(request):
    try:
        accountId = getIdByToken(request)
        account = AccountModel.objects.get(id = accountId)
        employee = EmployeeModel.objects.get(id = account.username)
        return JsonResponse({"name": employee.firstName + " " + employee.middleName + ' ' + employee.lastName})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})
