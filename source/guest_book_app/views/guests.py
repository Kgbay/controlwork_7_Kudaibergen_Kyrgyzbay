from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404

from guest_book_app.models import Guest


def guest_add_view(request: WSGIRequest):
    if request.method == "GET":
        guests = Guest.objects.all()
        context = {'guests': guests}
        return render(request, 'guest_create.html', context=context)
    guest_data = {
        'author': request.POST.get('author'),
        'mail': request.POST.get('mail'),
        'text': request.POST.get('text')
    }
    guest = Guest.objects.create(**guest_data)
    return redirect('index_view')

def guest_update_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == 'POST':
        guest.author = request.POST.get('author')
        guest.mail = request.POST.get('mail')
        guest.text = request.POST.get('text')
        guest.save()
        return redirect('index_view')
    return render(request, 'guest_update.html', context={
        'guest': guest
    })

def guest_remove_view(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    return render(request, 'guest_confirm_delete.html', context={'guest': guest})

def guest_confirm_remove(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    guest.delete()
    return redirect('index_view')