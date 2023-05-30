from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Entry

@csrf_exempt
def process(request):
    if request.method != 'GET':
        return HttpResponse("unsupported request type "+request.method)
    data = serializers.serialize( "python", Entry.objects.all() )
    if len(data) > 0:
        data = [i['fields'] for i in data]
        key = list(data[0].keys())[0]
        data = [i[key] for i in data]
        data = '\n'.join(data)
    else:
        data = ""
    response = f"<pre>{data}</pre>"
    return HttpResponse(response)
