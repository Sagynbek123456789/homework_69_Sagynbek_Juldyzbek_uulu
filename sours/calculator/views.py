import json
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


def data_checking(request_body) -> dict[str, str | float]:
    try:
        data = json.loads(request_body)
        data['A'], data['B'] = float(data['A']), float(data['B'])
    except json.decoder.JSONDecodeError:
        return {'error': 'Отправили некорректные данные не формате JSON'}
    except KeyError as e:
        return {'error': f'Отсутствует значение {e}'}
    except ValueError:
        return {'error': 'Входные данные должны быть числами'}
    return data


def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = data_checking(request.body)
        if 'error' in data:
            return JsonResponse(data, status=400)

        return JsonResponse({'answer': data["A"] + data["B"]})


def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = data_checking(request.body)
        if 'error' in data:
            return JsonResponse(data, status=400)

        return JsonResponse({'answer': data["A"] - data["B"]})


def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = data_checking(request.body)
        if 'error' in data:
            return JsonResponse(data, status=400)

        return JsonResponse({'answer': data["A"] * data["B"]})


def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = data_checking(request.body)
        if 'error' in data:
            return JsonResponse(data, status=400)
        try:
            return JsonResponse({'answer': data["A"] / data["B"]})
        except ZeroDivisionError:
            return JsonResponse({'error': 'Делить на ноль нельзя'}, status=400)

