from django.conf.urls import url
from customer import views


urlpatterns = [
    url(r"^customer_api$", views.customerApi)
]