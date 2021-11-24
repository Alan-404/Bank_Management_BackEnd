from django.conf.urls import url
from user import views

urlpatterns = [
    url(r"^user_api$", views.userApi)
]