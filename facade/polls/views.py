from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render

from .forms import TheForm

from .connection_to_logger import log_msg, get_msgs
from .connection_to_messages import messages_get
from .hazelcast_client import queue
from .get_all import get_all_msgs

def instruction(request):
    return HttpResponse("Welcome! go to polls/message to store a message, polls/database to see all messages")

def get_message(request):
    print("request", request)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("trying to send a message")
        # create a form instance and populate it with data from the request:
        form = TheForm(request.POST)
        # check whether it's valid:
        if not form.is_valid():
            return HttpRequest("invalid form")
        # process the data in form.cleaned_data as required
        msg = form.cleaned_data['msg']
        print("adding message to queue", queue.put(msg))
        if log_msg(msg):
            # redirect to a new URL:
            return HttpResponseRedirect('/polls/thanks')
        else:
            return HttpResponseRedirect('/polls/error')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = TheForm()
    
    return render(request, 'form.html', {'form': form})

def thank(request):
    return HttpResponse("Thank's for the message!")

def error(request):
    return HttpResponse("Message was not logged...")

def get_messages(request):
    if request.method == 'GET':
        return HttpResponse(get_msgs())
    return HttpResponse("Unsupported request method")

def messages_get_request(request):
    return HttpResponse(messages_get())

def get_all(request):
    return HttpResponse(f"<pre>{get_all_msgs()}</pre>")
