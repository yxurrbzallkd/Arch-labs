from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Entry
from django.core import serializers
from .connection_to_hazelcast import log_msg, get_msgs
import json
# Create your views here.
@csrf_exempt
def receive(request):
    if request.method == 'GET':
        data = get_msgs()
        return HttpResponse(data)
    if request.method != 'POST':
        return HttpResponse("unsupported method")
    # if a POST
    msg = json.loads(request.body)
    if not log_msg(msg):
        return HttpResponse("Message not logged")
    return HttpResponse("OK")
