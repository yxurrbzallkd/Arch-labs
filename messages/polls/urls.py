from . import views
from django.urls import path

urlpatterns = [
    path('', views.process, name='return-messages'),
]