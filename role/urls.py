from django.conf.urls import url
from role import views

urlpatterns = [
    url(r"^role_api$", views.roleApi)
]