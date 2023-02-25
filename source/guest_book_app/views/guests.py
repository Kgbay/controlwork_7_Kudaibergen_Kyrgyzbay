from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

def guest_add_view(request: WSGIRequest):
    return render(request, 'guest.html')