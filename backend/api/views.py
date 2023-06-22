from django.shortcuts import render
from django.http import JsonResponse
from django import views


class TestApi(views.View):
    def get(self, request):
        return JsonResponse({'test': 'wow'})
