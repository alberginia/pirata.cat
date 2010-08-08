from django.forms import models
from django.contrib import admin
from apps.contact.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body', 'timestamp')
    list_filter = ('name', 'email', 'body', 'timestamp')
    ordering = ('-timestamp', )
    date_hierarchy = 'timestamp'
    search_fields = ('name', 'email', 'body', 'timestamp')

admin.site.register(Message, MessageAdmin)

