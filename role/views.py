from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from role.serializer import RoleSerializer
from role.models import RoleModel
# Create your views here.

@api_view(['GET'])
def roleApi(request):
    if request.method == "GET":
        roles = RoleModel.objects.all()
        roles_serializer = RoleSerializer(roles, many=True)
        return JsonResponse({"roles": roles_serializer.data})


