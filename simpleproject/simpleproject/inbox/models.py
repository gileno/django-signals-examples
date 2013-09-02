#encoding: utf-8

from django.db import models
from django.conf import settings

from .signals import message_created


class Message(models.Model):

    subject = models.CharField(max_length=255)
    message = models.TextField(blank=True)

    sent_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=u'Sent by', related_name='sent'
    )
    to = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name=u'To', related_name='inbox'
    )

    submitted = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)
        message_created.send(sender=self)

    def __unicode__(self):
        return self.subject

    class Meta:
        ordering = ['-submitted']


def new_message(sender, **kwargs):
    print sender
    print kwargs['instance']
models.signals.post_save.connect(
    new_message, dispatch_uid='inbox_new_message'
)

def delete_message(sender, **kwargs):
    raise Exception(u'Não')
models.signals.pre_delete.connect(
    delete_message, sender=Message, dispatch_uid='inbox_delete_message'
)