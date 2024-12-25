from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_admin, name = 'login_admin'),
    path('logout/', views.logout_admin, name = 'logout_admin'),
    path('', views.home, name = 'home'),
    path('projects/', views.projects, name = 'projects'),
    path('blogs/', views.blogs, name = 'blogs'),
    path('blogs/create/', views.create_blog, name = 'create_blog'),
    path('blogs/delete/<int:pk>/', views.delete_blog_with_pk, name = 'delete_blog_with_pk'),
    path('blogs/delete/', views.delete_blog, name = 'delete_blog'),
    path('blogs/edit/<int:pk>/', views.edit_blog, name = 'edit_blog'),
    path('file_manager/', views.file_manager, name = 'file_manager'),
    path('file_manager/delete/<int:pk>/', views.delete_file, name = 'delete_file'),
    path('languages/delete/<int:pk>/', views.delete_language, name = 'delete_language'),
    path('newsletters/delete/<int:pk>/', views.delete_newsletter, name = 'delete_newsletter'),
    path('testimonials/delete/<int:pk>/', views.delete_testimonial, name = 'delete_testimonial'),
    path('projects/delete/', views.delete_project, name = 'delete_project'),
    path('projects/delete/<int:pk>/', views.delete_project_with_pk, name = 'delete_project_with_pk'),
    path('projects/create/', views.create_project, name = 'create_project'),
    path('projects/edit/<int:pk>/', views.edit_project, name = 'edit_project'),
]