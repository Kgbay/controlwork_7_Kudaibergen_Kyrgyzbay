from django.contrib import admin

from .models import Guest


# Register your models here.
class GuestAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'mail')
    list_filter = ('id', 'author', 'created_at')
    search_fields = ('author', 'text')
    fields = ('author', 'mail', 'text', 'status')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Guest, GuestAdmin)