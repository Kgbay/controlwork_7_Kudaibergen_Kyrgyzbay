from django.urls import path

from .views.base import index_view
from .views.guests import guest_add_view, guest_update_view, guest_remove_view

urlpatterns = [
    path("", index_view, name='index_view'),
    path("guest/add/", guest_add_view, name="guest_add"),
    path("guest/<int:pk>/update/", guest_update_view, name="guest_edit"),
    path("guest/<int:pk>/remove/", guest_remove_view, name="guest_remove")
]