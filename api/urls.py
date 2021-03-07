from django.urls import path

from api.views import base_view

urlpatterns = [
    path('', base_view)
]