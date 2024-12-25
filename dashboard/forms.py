from .models import *
from django import forms
from django.core.validators import FileExtensionValidator

class TestimonialForm(forms.Form):
    
    name = forms.CharField(
        max_length = 50,
        widget = forms.TextInput(attrs = {'class': 'text-sm w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Name'}),
        label = 'Name',
        required = True
    )

    message = forms.CharField(
        widget = forms.Textarea(attrs = {'class': 'text-sm w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Message'}),
        label = 'Message',
        required = True
    )

    position = forms.CharField(
        widget = forms.TextInput(attrs = {'class': 'text-sm w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Position'}),
        label = 'Position',
        required = True
    )

    company = forms.CharField(
        widget = forms.TextInput(attrs = {'class': 'text-sm w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Company'}),
        label = 'Company',
        required = True
    )

    image = forms.ImageField(
        widget = forms.ClearableFileInput(attrs = {'multiple': False, 'class': 'w-full shadow-inner flex border cursor-pointer text-sm rounded focus:outline-none focus:outline-indigo-500 bg-transparent file:bg-transparent file:border-0 py-1 px-2'}),
        label = 'Image',
        required = True,
        validators=[FileExtensionValidator(allowed_extensions = ['jpg', 'jpeg', 'png', 'gif', 'svg'])]
    )

class LanguageForm(forms.Form):

    name = forms.CharField(
        max_length=50,
        widget = forms.TextInput(attrs={'class': 'text-sm w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Name'}),
        label = 'Name',
        required = True
    )

    short_description = forms.CharField(
        widget = forms.TextInput(attrs = {'class': 'text-sm w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Short Description'}),
        label = 'Short Description',
        required = True,
        max_length = 50
    )

    background_color = forms.CharField(
        widget = forms.TextInput(attrs = {'class': 'text-sm w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Background Color'}),
        label = 'Background Color',
        required = True,
        max_length = 50
    )

    image = forms.ImageField(
        widget = forms.ClearableFileInput(attrs={'multiple': False, 'class': 'w-full shadow-inner flex border cursor-pointer text-sm rounded focus:outline-none focus:outline-indigo-500 bg-transparent file:bg-transparent file:border-0 py-1 px-2'}),
        label = 'Image',
        required = True,
        validators=[FileExtensionValidator(allowed_extensions = ['jpg', 'jpeg', 'png', 'gif', 'svg'])]
    )

class UploadedAssetForm(forms.Form):
    file = forms.FileField(
        widget = forms.ClearableFileInput(attrs = {'multiple': False, 'class': 'w-full shadow-inner flex border cursor-pointer text-sm rounded focus:outline-none focus:outline-indigo-500 bg-transparent file:bg-transparent file:border-0 py-1 px-2'}),
        label = 'File',
        required = True
    )

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'subheading', 'image', 'content', 'published']
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Title'}),
            'subheading': forms.TextInput(attrs = {'class': 'w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Subheading'}),
            'image': forms.ClearableFileInput(attrs = {'multiple': False, 'class': 'w-full shadow-inner mb-2 flex border cursor-pointer rounded focus:outline-none focus:outline-indigo-500 bg-transparent file:bg-transparent file:border-0 py-1 px-2'}),
            'content': forms.Textarea(attrs = {'class': 'w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Content'}),
            'published': forms.CheckboxInput(attrs = {'class': ''})
        }
        labels = {
            'title': 'Title',
            'subheading': 'Subheading',
            'image': 'Image',
            'content': 'Content',
            'published': 'Published'
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['heading', 'sub_heading', 'description', 'image', 'name', 'demo_url', 'source_url', 'languages', 'published']
        widgets = {
            'heading': forms.TextInput(attrs = {'class': 'w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Heading'}),
            'sub_heading': forms.TextInput(attrs = {'class': 'w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Sub Heading'}),
            'description': forms.Textarea(attrs = {'class': 'w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Description'}),
            'image': forms.ClearableFileInput(attrs = {'multiple': False, 'class': 'w-full shadow-inner mb-2 flex border cursor-pointer rounded focus:outline-none focus:outline-indigo-500 bg-transparent file:bg-transparent file:border-0 py-1 px-2'}),
            'name': forms.TextInput(attrs = {'class': 'w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Name'}),
            'demo_url': forms.URLInput(attrs = {'class': 'w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Demo URL'}),
            'source_url': forms.URLInput(attrs = {'class': 'w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500', 'placeholder': 'Source URL'}),
            'languages': forms.SelectMultiple(attrs = {'class': 'w-full border py-1 px-2 rounded mb-2 shadow-inner focus:outline-none focus:outline-indigo-500'}),
            'published': forms.CheckboxInput(attrs = {'class': 'my-2 mb-4'})
        }
        labels = {
            'heading': 'Heading',
            'sub_heading': 'Sub Heading',
            'description': 'Description',
            'image': 'Image',
            'name': 'Name',
            'demo_url': 'Demo URL',
            'source_url': 'Source URL',
            'languages': 'Languages',
            'published': 'Published'
        }



