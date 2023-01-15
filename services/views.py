from django.shortcuts import render
from services.forms import NewsletterSubscriptionForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.contrib import messages
from django.template.loader import render_to_string
from django.views import generic

from weather import settings


class NewsletterSubscription(generic.View):
    email_template = 'services/newsletter.html'
    template_name = 'main/index.html'

    def post(self, request):
        form = NewsletterSubscriptionForm(request.POST)
        current_site = get_current_site(request)

        if form.is_valid():
            # Save email in db after email is sent
            form.save(commit=False)

            # Send mail
            status = self.send_email(request.POST.get('email'), current_site)

            if status:
                # Save email to db
                form.save(commit=True)

                message = messages.add_message(
                    request, messages.SUCCESS, 'An Email has been sent to your account.'
                )

                return render(request, self.template_name, {'message': message})
            else:
                message = messages.add_message(
                    request, messages.ERROR, 'Error validating email'
                )

                return render(request, self.template_name, {'message': message})
        else:
            message = messages.add_message(
                request, messages.ERROR, 'Error validating email'
            )

            return render(request, self.template_name, {'message': message})

    def send_email(self, address, current_site):

        subject = 'NEWSLETTER SUBSCRIPTION'
        context = {
            'email': address,
            'current_site': current_site,
        }
        email = render_to_string(self.email_template, context)

        try:
            send_mail(
                subject, email, settings.EMAIL_HOST_USER,
                [address], fail_silently=False,html_message=email
            )

            return True
        except BadHeaderError:
            return False



