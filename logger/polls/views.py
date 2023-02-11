from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Entry
from django.core import serializers
import json
# Create your views here.
@csrf_exempt
def receive(request):
    if request.method == 'GET':
        data = serializers.serialize( "python", Entry.objects.all() )
        if len(data) == 0:
            data = "no data yet"
        else:
            data = [i['fields'] for i in data]
            keys = list(data[0].keys())[:2]
            keys = keys[0].rjust(10) + " " + keys[1]
            data = [[i[k] for k in i] for i in data]
            #data = [str(i[0]).rjust(10)+" "+i[1] for i in data]
            data = [i[1] for i in data]
            #data = [keys]+data
            #response = f"<pre>{json.dumps(data, indent=1)}</pre>"
            data = '\n'.join(data)
        response = f"<pre>{data}</pre>"
        return HttpResponse(response)
    if request.method != 'POST':
        return HttpResponse("unsupported method")
    # if a POST
    msg = json.loads(request.body)
    entry = Entry.objects.create(UUID=msg['UUID'], msg=msg['msg'])
    print(msg)
    return HttpResponse("OK")
