from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from django.contrib.auth.hashers import make_password, check_password

from account.serializer import AccountSerializer
from account.models import AccountModel
from common.constants import Constants
from user.models import UserModel
from user.serializer import UserSerializer
from common.lib import getIdByToken, makeAccessToken

# Create your views here.


@api_view(['GET', 'POST'])
def accountApi(request):   
    if request.method == "GET":
        accounts = AccountModel.objects.all()
        accounts_serializer = AccountSerializer(accounts, many=True)
        return JsonResponse({"accounts": accounts_serializer.data}, )
    elif request.method == "POST":
        try:
            account_data = JSONParser().parse(request);
            account_data["password"] = make_password(account_data["password"])
            account_serializer = AccountSerializer(data = account_data)
            if account_serializer.is_valid():
                account_serializer.save()
                return JsonResponse({"success": True}, )
            return JsonResponse({"success": True}, )
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, )
 


@api_view(["DELETE"])
def deleteAccount(request, accountId):
    if request.method == "DELETE":
        try:
            account = AccountModel.objects.get(id = accountId)
            account.delete()
            return JsonResponse({"success": True}, )
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})


@api_view(['POST'])
def loginAccount(request):
    try:
        account_data = JSONParser().parse(request)
        account = AccountModel.objects.get(email = account_data["email"])   
        if account == None:
            return JsonResponse({"success": False})
        
        if check_password(account_data["password"], account.password):
            token = makeAccessToken(account)
            return JsonResponse({"success": True, "accessToken": token})
        return JsonResponse({"success": False, "message": "Invalid username or password"})
    except Exception as e:
        return JsonResponse({"success": False, "message": "Invalid username or password: " + str(e)})


@api_view(["PUT"])
def changePassword(request):
    try:
        account_data = JSONParser().parse(request)     
        accountId = getIdByToken(request)
        account = AccountModel.objects.get(id = accountId)
        if check_password(account_data["oldPassword"], account.password) is False:
            return JsonResponse({"success": False, "message": 'invalid account'} )
        account_obj = {
            "id": accountId,
            "email": account.email,
            "password": make_password(account_data["newPassword"])
        }
        account_serializer = AccountSerializer(account, data=account_obj)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse({"success": True}, )
        return JsonResponse({"success": False}, )
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)} )
    

@api_view(['GET'])
def authToken(request):
    try:
        accountId = getIdByToken(request)
        account = AccountModel.objects.get(id=accountId)
        if account is None:
            return JsonResponse({"message": "invalid account"})
        user = UserModel.objects.get(email = account.email)
        user_serializer = UserSerializer(user)
        if user is not None:
            return JsonResponse({"user": user_serializer.data})
        return JsonResponse({"message": "invalid account"})
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)} )

