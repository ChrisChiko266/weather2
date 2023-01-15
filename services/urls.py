from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('newsletter/subscription/', views.NewsletterSubscription.as_view(), name='news-sub'),
]