#encoding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from .views import InboxView

urlpatterns = patterns('',
    url('^$', login_required(InboxView.as_view()), name='inbox')
)