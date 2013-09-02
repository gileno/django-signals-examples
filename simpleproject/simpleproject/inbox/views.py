#encoding: utf-8

from django.views.generic import TemplateView


class InboxView(TemplateView):

    template_name = 'inbox/index.html'