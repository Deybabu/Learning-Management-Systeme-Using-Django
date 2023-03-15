from django.urls import path

from user.views import sample, user_login

app_name = "user"

urlpatterns = [
    path('', sample, name="sample"),
    path('login/', user_login, name="login"),
]
