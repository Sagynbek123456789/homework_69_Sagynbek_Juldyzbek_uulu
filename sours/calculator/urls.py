from django.urls import path
from calculator.views import add_view, subtract_view, divide_view, multiply_view

app_name = 'calculator'

urlpatterns = [
    path('add/', add_view, name='add'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name='divide')
]