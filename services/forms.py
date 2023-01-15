from django import forms 
from .models import NewsletterSubscriptions


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriptions
        fields = ('email',)
