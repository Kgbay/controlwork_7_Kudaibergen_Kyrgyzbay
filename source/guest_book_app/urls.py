from django.urls import path

from .views.base import index_view
from .views.guests import guest_add_view

urlpatterns = [
    path("", index_view, name='index_view')
]