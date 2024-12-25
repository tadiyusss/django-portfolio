from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *
from django_portfolio.models import *
from request.models import Request
from datetime import date

def login_admin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'authentication/login.html')

def logout_admin(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login_admin')
    else:
        return HttpResponse('You are not logged in')


@login_required(login_url = 'login_admin')
def home(request):
    language_form = LanguageForm()
    testimonial_form = TestimonialForm()
    testmonials = Testimonial
    languages = Language
    newsletter = Newsletter
    hit_counts = Request

    today = date.today()
    hit_counter = {
        'hits_today': Request.objects.filter(time__date = today),
        'hits_total': Request.objects.all(),
        'hits_unique_today': Request.objects.filter(time__date = today).values('ip').annotate(Count('ip')),
        'most_visited_page': Request.objects.values('path').annotate(Count('path')).order_by('-path__count').first()

    }

    context = {
        'testimonial_form': testimonial_form,
        'language_form': language_form,
        'testimonials': testmonials.objects.all(),
        'languages': languages.objects.all(),
        'newsletter': newsletter.objects.all(),
        'hit_counter': hit_counter
    }

    if request.method == 'POST':
        if 'add_testimonial' in request.POST:
            testimonial_form = TestimonialForm(request.POST, request.FILES)

            if testimonial_form.is_valid():
                name = testimonial_form.cleaned_data['name']
                message = testimonial_form.cleaned_data['message']
                position = testimonial_form.cleaned_data['position']
                company = testimonial_form.cleaned_data['company']
                image = testimonial_form.cleaned_data['image']
                testimonial = Testimonial(name=name, message=message, position=position, company=company, image=image)
                testimonial.save()
                messages.success(request, 'Testimonial added successfully')
            else:
                error = testimonial_form.errors.as_data()
                for key, value in error.items():
                    messages.error(request, f"{key}: {value[0].message}")

                return render(request, 'dashboard/home.html', context)

        if 'add_language' in request.POST:
            language_form = LanguageForm(request.POST, request.FILES)
            
            if language_form.is_valid():
                image = language_form.cleaned_data['image']
                name = language_form.cleaned_data['name']
                short_description = language_form.cleaned_data['short_description']
                background_color = language_form.cleaned_data['background_color']
                language = Language(image=image, name=name, short_description=short_description, background_color=background_color)
                language.save()
                messages.success(request, 'Language added successfully')
            else:
                error = language_form.errors.as_data()
                for key, value in error.items():
                    messages.error(request, f"{key}: {value[0].message}")

                return render(request, 'dashboard/home.html', context)

    return render(request, 'dashboard/home.html', context)

@login_required(login_url = 'login_admin')
def delete_file(request, pk):
    file = UploadedAsset.objects.filter(file_id = pk).first()
    if file:
        file.delete()
        messages.success(request, 'File deleted successfully')
    else:
        messages.error(request, 'File not found')
    return redirect('file_manager')

@login_required(login_url = 'login_admin')
def file_manager(request):
    form = UploadedAssetForm()
    files = UploadedAsset
    context = {
        'form': form,
        'files': files.objects.all()
    }

    if request.method == 'POST' and 'file_upload' in request.POST:
        form = UploadedAssetForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            uploaded_file = UploadedAsset(file=file)
            uploaded_file.save()
            messages.success(request, 'File uploaded successfully')
        else:
            error = form.errors.as_data()
            for key, value in error.items():
                messages.error(request, f"{key}: {value[0].message}")

            return render(request, 'dashboard/file_manager.html', context)

    return render(request, 'dashboard/file_manager.html', context)

@login_required(login_url = 'login_admin')
def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'dashboard/projects/projects.html', context)

@login_required(login_url = 'login_admin')
def blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'dashboard/blogs/blogs.html', context)


@login_required(login_url = 'login_admin')
def delete_blog(request):
    messages.success(request, 'You must select a blog ID to delete')
    return redirect('blogs')

@login_required(login_url = 'login_admin')
def delete_blog_with_pk(request, pk):
    blog = Blog.objects.get(blog_id = pk)
    if blog:
        blog.delete()
        messages.success(request, 'Blog deleted successfully')
    else:
        messages.error(request, 'Blog not found')
    return redirect('blogs')

@login_required(login_url = 'login_admin')
def edit_blog(request, pk):
    blog = Blog.objects.get(blog_id = pk)
    form = BlogForm(instance = blog)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance = blog)
        if form.is_valid() == False:
            error = form.errors.as_data()
            for key, value in error.items():
                messages.error(request, f"{key}: {value[0].message}")

        blog.title = form.cleaned_data['title']
        blog.subheading = form.cleaned_data['subheading']
        blog.image = form.cleaned_data['image']
        blog.content = form.cleaned_data['content']
        blog.published = form.cleaned_data['published']
        blog.save()
        context['form'] = form

        messages.success(request, 'Blog updated successfully')

    return render(request, 'dashboard/blogs/create.html', context)

@login_required(login_url = 'login_admin')
def create_blog(request):
    form = BlogForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        
        if form.is_valid() == False:
            error = form.errors.as_data()
            for key, value in error.items():
                messages.error(request, f"{key}: {value[0].message}")

        title = form.cleaned_data['title']
        subheading = form.cleaned_data['subheading']
        image = form.cleaned_data['image']
        content = form.cleaned_data['content']
        publish = 'publish_blog' in request.POST

        blog = Blog(title=title, subheading=subheading, image=image, content=content, published=publish)
        blog.save()
        messages.success(request, 'Blog created successfully')
        return redirect('blogs')

    return render(request, 'dashboard/blogs/create.html', context)

@login_required(login_url = 'login_admin')
def delete_language(request, pk):
    language = Language.objects.get(language_id = pk)
    language.delete()
    messages.success(request, 'Language deleted successfully')
    return redirect('home')

@login_required(login_url = 'login_admin')
def delete_newsletter(request, pk):
    newsletter = Newsletter.objects.get(newsletter_id = pk)
    newsletter.delete()
    messages.success(request, 'Newsletter deleted successfully')
    return redirect('home')

@login_required(login_url = 'login_admin')
def delete_project_with_pk(request, pk):
    project = Project.objects.get(project_id = pk)
    project.delete()
    messages.success(request, 'Project deleted successfully')
    return redirect('projects')

@login_required(login_url = 'login_admin')
def delete_project(request):
    return redirect('projects')

@login_required(login_url = 'login_admin')
def delete_testimonial(request, pk):
    testimonial = Testimonial.objects.get(testimonial_id = pk)
    testimonial.delete()
    messages.success(request, 'Testimonial deleted successfully')
    return redirect('home')

@login_required(login_url = 'login_admin')
def create_project(request):
    form = ProjectForm()
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid() == False:
            error = form.errors.as_data()
            for key, value in error.items():
                messages.error(request, f"{key}: {value[0].message}")

        heading = form.cleaned_data['heading']
        sub_heading = form.cleaned_data['sub_heading']
        description = form.cleaned_data['description']
        image = form.cleaned_data['image']
        name = form.cleaned_data['name']
        demo_url = form.cleaned_data['demo_url']
        source_url = form.cleaned_data['source_url']
        languages = form.cleaned_data['languages']
        published = 'publish_project' in request.POST

        project = Project(heading=heading, sub_heading=sub_heading, description=description, image=image, name=name, demo_url=demo_url, source_url=source_url, published=published)
        project.save()
        project.languages.set(languages)
        messages.success(request, 'Project created successfully')
        return redirect('projects')

    return render(request, 'dashboard/projects/create.html', context)

@login_required(login_url = 'login_admin')
def edit_project(request, pk):
    project = Project.objects.get(project_id = pk)
    form = ProjectForm(instance = project)
    context = {
        'form': form
    }

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance = project)
        if form.is_valid() == False:
            error = form.errors.as_data()
            for key, value in error.items():
                messages.error(request, f"{key}: {value[0].message}")

        project.heading = form.cleaned_data['heading']
        project.sub_heading = form.cleaned_data['sub_heading']
        project.description = form.cleaned_data['description']
        project.image = form.cleaned_data['image']
        project.name = form.cleaned_data['name']
        project.demo_url = form.cleaned_data['demo_url']
        project.source_url = form.cleaned_data['source_url']
        project.published = form.cleaned_data['published']
        project.languages.set(form.cleaned_data['languages'])
        project.save()
        context['form'] = form

        messages.success(request, 'Project updated successfully')

    return render(request, 'dashboard/projects/create.html', context)