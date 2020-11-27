from apps.chat.views import home
from django.urls import path

app_name = "chat"

urlpatterns = [path("", home)]
