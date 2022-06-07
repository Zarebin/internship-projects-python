from django.shortcuts import render

from django.http import JsonResponse


def test(request):
    return JsonResponse({'message': 'food_label app created'})
