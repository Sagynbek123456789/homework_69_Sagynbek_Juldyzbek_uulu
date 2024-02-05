import json
from django.http import JsonResponse


def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse(data)


def subtract_view(request, *args, **kwargs):
    pass


def multiply_view(request, *args, **kwargs):
    pass


def divide_view(request, *args, **kwargs):
    pass

