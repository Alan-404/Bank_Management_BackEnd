from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse 

from django.contrib.auth.hashers import make_password

from employee.models import EmployeeModel
from employee.serializer import EmployeeSerializer
from account.serializer import AccountSerializer
from account.models import AccountModel
from user.serializer import UserSerializer

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
            user_serializer = UserSerializer(data={"cId": employee_data["cId"],"firstName": employee_data["firstName"], "middleName": employee_data["middleName"], "lastName": employee_data["lastName"], "bDate": employee_data["bDate"], "phone": employee_data["phone"], "address": employee_data["address"], "avatar": employee_data["avatar"], "email": employee_data["email"], "role": 2})
            if user_serializer.is_valid():
                user_serializer.save()
                print(user_serializer["id"].value)
                employee_serializer = EmployeeSerializer(data={"id": "EMP_"+ str(user_serializer["id"].value), "emailWork":"emp_" + str(user_serializer["id"].value) + "@alpo.com", "userId": user_serializer["id"].value})
                if employee_serializer.is_valid():
                    employee_serializer.save()
                    hashPassword = make_password("123")
                    account_serializer = AccountSerializer(data={"email": employee_serializer["emailWork"].value, "password": hashPassword})
                    if account_serializer.is_valid():
                        account_serializer.save()
                        return JsonResponse({"sucess": True})
            return JsonResponse({"success": False})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})




@api_view(["GET"])
def getNameByToken(request):
    try:
        accountId = getIdByToken(request)
        account = AccountModel.objects.get(id = accountId)
        employee = EmployeeModel.objects.get(id = account.username)
        return JsonResponse({"name": employee.firstName + " " + employee.middleName + ' ' + employee.lastName})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)})
