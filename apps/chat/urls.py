from apps.chat.views import home, room
from django.urls import path

app_name = "chat"

urlpatterns = [path("", home), path("<str:room_name>/", room)]
