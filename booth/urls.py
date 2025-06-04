from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('class', views.IndexView.as_view(), name='class'),
]