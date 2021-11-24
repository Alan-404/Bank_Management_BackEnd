from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from banner.models import BannerModel
from banner.serializer import BannerSerializer
# Create your views here.

@api_view(["GET","POST"])
def bannerApi(request):
    if request.method == "GET":
        try:
            banners = BannerModel.objects.all()
            banners_serializer = BannerSerializer(banners, many=True)
            return JsonResponse({"banners": banners_serializer.data})
        except Exception as e:
            return JsonResponse({"message": str(e)})
    elif request.method == "POST":
        try:
            banner_data = JSONParser().parse(request)
            banner_serializer = BannerSerializer(data=banner_data)
            if banner_serializer.is_valid():
                banner_serializer.save()
                return JsonResponse({"success": True})
            return JsonResponse({"success": False})
        except Exception as e:
            print(str(e))