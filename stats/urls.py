from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('predictions/', views.forebet_predictions, name='predictions')
]