from django.urls import path

from .views.base import index_view
from .views.guests import guest_add_view, guest_update_view, guest_remove_view, guest_confirm_remove

urlpatterns = [
    path("", index_view, name='index_view'),
    path("guest/add/", guest_add_view, name="guest_add"),
    path("guest/<int:pk>/update/", guest_update_view, name="guest_edit"),
    path("guest/<int:pk>/remove/", guest_remove_view, name="guest_remove"),
    path("guest/<int:pk>/confirm_remove/", guest_confirm_remove, name='guest_remove_confirm')
]