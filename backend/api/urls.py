from django.urls import path
from .views import TestApi

urlpatterns = [
    path('', TestApi.as_view()),
]
