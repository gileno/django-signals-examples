#encoding: utf-8

from django.contrib import admin

from .models import Message


class MessageAdmin(admin.ModelAdmin):

    list_display = ['subject', 'sent_by', 'to', 'submitted']
    search_fields = ['subject', 'sent_by__username', 'to__username']


admin.site.register(Message, MessageAdmin)