from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from user.models import UserModel
from user.serializer import UserSerializer
# Create your views here.


@api_view(["GET", "POST"])
def userApi(request):
    if request.method == "GET":
        try:
            users = UserModel.objects.all()
            users_serializer = UserSerializer(users, many=True)
            return JsonResponse({"users": users_serializer.data})
        except Exception as e:
            return JsonResponse({"message": str(e)})
    elif request.method == "POST":
        try:
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(data = user_data)
            if user_serializer.is_valid():
                user_serializer.save()
                return JsonResponse({"success": True})
            return JsonResponse({"success": False})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})
