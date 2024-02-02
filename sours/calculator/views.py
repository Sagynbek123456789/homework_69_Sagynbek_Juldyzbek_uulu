import json
from urllib import request
from django.http import JsonResponse, HttpResponseBadRequest
from django.http import HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie
from flask import Flask, jsonify


def get_token_view(request, *args, **kwargs):
    if request.method == 'POST':
        return HttpResponse()
    return HttpResponseNotAllowed(['POST'])


def add_view(request):
    if request.method == 'POST':
        try:
            A = 1234
            B = 4567

            result = {
                'answer': A + B
            }
            return JsonResponse(result)
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({'error': str(e)}), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({'error': 'Метод не разрешен'}), content_type='application/json')


def subtract_view(request):
    if request.method == 'POST':
        try:

            A = 1234
            B = 4567

            result = {
                'answer': A - B
            }
            return JsonResponse(result)
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({'error': str(e)}), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({'error': 'Метод не разрешен'}), content_type='application/json')


def multiply_view(request):
    if request.method == 'POST':
        try:

            A = 1234
            B = 4567

            if A == 0 or B == 0:
                raise ValueError("Multiplication by zero!")

            result = {
                'answer': A * B
            }
            return JsonResponse(result)
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({'error': str(e)}), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({'error': 'Метод не разрешен'}), content_type='application/json')


def divide_view(request):
    if request.method == 'POST':
        try:

            A = 1234
            B = 4567

            if A == 0 or B == 0:
                raise ValueError("Division by zero!")

            result = {
                'answer': A / B
            }
            return JsonResponse(result)
        except Exception as e:
            return HttpResponseBadRequest(json.dumps({'error': str(e)}), content_type='application/json')

    else:
        return HttpResponseBadRequest(json.dumps({'error': 'Метод не разрешен'}), content_type='application/json')



