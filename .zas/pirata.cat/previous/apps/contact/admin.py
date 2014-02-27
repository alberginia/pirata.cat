from django.forms import models
from django.contrib import admin
from apps.contact.models import Message, Interested


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body', 'timestamp')
    list_filter = ('email', 'timestamp')
    ordering = ('-timestamp', )
    date_hierarchy = 'timestamp'
    search_fields = ('name', 'email', 'body', 'timestamp')
    
class InterestedAdmin(admin.ModelAdmin):
    list_display = ('email', 'timestamp', 'added')
    list_filter = ('email', 'timestamp', 'added')
    ordering = ('-timestamp', )
    date_hierarchy = 'timestamp'
    search_fields = ('email', 'timestamp', 'added')


admin.site.register(Message, MessageAdmin)
admin.site.register(Interested, InterestedAdmin)

