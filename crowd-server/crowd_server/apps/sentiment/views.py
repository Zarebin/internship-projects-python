from django.shortcuts import render
from django.http import JsonResponse


def test(request):
    return JsonResponse({'message': 'sentiment app created'})
