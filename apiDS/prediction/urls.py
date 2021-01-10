from django.urls import path
from .views import Pred, Result

urlpatterns = [
    path('pred/', Pred, name = 'Pred'),
    path('result/', Result, name = 'Result')
]