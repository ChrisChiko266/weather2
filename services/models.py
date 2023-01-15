from django.db import models
from django.utils.translation import gettext_lazy as _


# Table holds info on newsletter subscriptions
class NewsletterSubscriptions(models.Model):
    class Meta:
        verbose_name = 'Newsletter Subscription'
        verbose_name_plural = 'Newsletter Subscriptions'

    email = models.EmailField(_("Email"), blank=True, unique=True)
    date = models.DateTimeField(_("Subscription Date"), auto_now=True)

    def __str__(self):
        return '{}'.format(self.email)
