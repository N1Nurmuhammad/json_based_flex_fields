# app/api_urls.py
from django.urls import path

from v1.views import get_public_items

app_name = "v1"

urlpatterns = [
    path("/get-items/<str:lang>", get_public_items, name="get_public_items"),
]
