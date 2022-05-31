from django.shortcuts import render
from django.http import JsonResponse


def test(request):
    return JsonResponse({'message' : 'Image Label Verification Project Starting ...'})
