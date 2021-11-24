from django.conf.urls import url
from banner import views


urlpatterns=[
    url(r"^banner_api$", views.bannerApi)
]