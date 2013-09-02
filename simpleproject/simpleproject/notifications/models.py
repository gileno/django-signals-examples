#encoding: utf-8

from django.db import models
from django.conf import settings

from simpleproject.inbox.signals import message_created
from simpleproject.inbox.models import Message


class Notification(models.Model):

    target = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='notifications'
    )
    title = models.CharField(max_length=255)
    message = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.target, self.title)

    class Meta:
        ordering = ['-created_on']


def new_notifications(sender, **kwargs):
    pass #send mail
models.signals.post_save.connect(
    new_notifications, sender=Notification, 
    dispatch_uid='notifications_new_notification'
)

def message_created_notification(sender, **kwargs):
    print 'aki :)'
message_created.connect(message_created_notification, 
    sender=Message, dispatch_uid='message_created_notification')