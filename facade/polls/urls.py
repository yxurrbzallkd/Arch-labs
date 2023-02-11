from django.urls import path

from . import views

urlpatterns = [
    path('help', views.instruction, name='instructions'),
    path('', views.get_message, name='message-form'),
    path('thanks', views.thank, name='thank-you'),
    path('error', views.error, name='log-error'),
    path('database', views.get_messages, name='get-messages'),
    path('messages', views.messages_get_request, name='messages')
]