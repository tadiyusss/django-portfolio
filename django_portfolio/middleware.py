from .forms import NewsletterForm
from .models import Newsletter
from django.contrib import messages
from django.shortcuts import redirect

class NewsletterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST" and 'newsletter_form' in request.POST:
            # check if email is already in the database
            email = request.POST['email']
            form = NewsletterForm(request.POST)
            if Newsletter.objects.filter(email=email).exists():
                messages.info(request, 'You are already subscribed to the newsletter.')
            elif form.is_valid():
                form.save()
                messages.success(request, 'You have successfully subscribed to the newsletter.')   
                return redirect(request.path + '#newsletter')
        return self.get_response(request)