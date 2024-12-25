from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from dashboard.models import *

def index(request):
    languages = Language.objects.all()
    projects = Project.objects.filter(published=True)
    testimonials = Testimonial.objects.all()
    blogs = Blog.objects.filter(published=True)
    context = {
        'languages': languages,
        'projects': projects,
        'testimonials': testimonials,
        'blogs': blogs
    }
    return render(request, 'index.html', context)

def project_detail(request, project_id):
    project = get_object_or_404(Project, published=True, project_id=project_id)

    context = {
        'project': project
    }
    
    return render(request, 'project_details.html', context)

def view_blog(request, blog_id):
    blog = get_object_or_404(Blog, blog_id = blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'view_blog.html', context)
    