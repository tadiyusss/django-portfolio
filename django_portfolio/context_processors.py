from .forms import NewsletterForm
from django.contrib.messages import get_messages
from dashboard.models import Project

def list_messages(request):
    storage = get_messages(request)
    return {'messages': storage}

def newsletter_form(request):
    return {'newsletter_form': NewsletterForm()}

def get_projects(request):
    # get the top 3 projects
    projects = Project.objects.all()
    return {
        'footer_projects': projects
    }