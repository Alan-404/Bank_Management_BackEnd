from django.conf.urls import url
from account import views

urlpatterns = [
    url(r"^account_api$", views.accountApi),
    url(r"^delete_account/(?P<accountId>\w+)$", views.deleteAccount),
    url(r"login", views.loginAccount),
    url(r"^change_password$", views.changePassword),
    url(r"^auth$", views.authToken)
]