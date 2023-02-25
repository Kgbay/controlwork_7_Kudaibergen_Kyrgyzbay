from django.shortcuts import render

from guest_book_app.models import Guest

# Create your views here.
def index_view(request):
    guests = Guest.objects.exclude(is_deleted=True)
    context = {
        'guests': guests
    }
    return render(request, 'index.html', context=context)