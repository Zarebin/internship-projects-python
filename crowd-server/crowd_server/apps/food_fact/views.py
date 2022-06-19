from django.http import JsonResponse


def test(request):
    return JsonResponse({'message' : 'food_fact Verification Project Starting ...'})
