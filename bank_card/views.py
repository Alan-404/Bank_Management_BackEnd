from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse


from bank_card.models import BankCardModel
from bank_card.serializer import BankCardSerializer
# Create your views here.


@api_view(['GET'])
def bankCardApi(request):
    if request.method == "GET":
        try:
            bankCards = BankCardModel.objects.all()
            bankCards_serializer = BankCardSerializer(data=bankCards, many=True)
            return JsonResponse({"bankCards": bankCards_serializer.data})
        except Exception as e:
            return JsonResponse({"message": str(e)})

