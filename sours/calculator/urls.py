from django.urls import path
from calculator.views import add_view, get_token_view, subtract_view, multiply_view, divide_view


app_name = 'calculator'

urlpatterns = [
    path('add/', add_view, name='add_view'),
    path('subtract/', subtract_view, name='subtract_view'),
    path('multiply/', multiply_view, name='multiply_view'),
    path('divide/', divide_view, name='divide_view'),
    path('token/', get_token_view, name='get_token'),
]
