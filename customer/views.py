from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from customer.models import CustomerModel
from customer.serializer import CustomerSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def customerApi(request):
    if request.method == "GET":
        try:
            customers = CustomerModel.objects.all()
            customers_serializer = CustomerSerializer(customers, many=True)
            return JsonResponse({"customers": customers_serializer.data})
        except Exception as e:
            return JsonResponse({"message": str(e)})
    elif request.method == "POST":
        try:
            customer_data = JSONParser().parse(request)
            customer_serializer = CustomerSerializer(data=customer_data)
            if customer_serializer.is_valid():
                customer_serializer.save()
                return JsonResponse({"success": True})
        except Exception as e:
                return JsonResponse({"success": False, "message": str(e)})