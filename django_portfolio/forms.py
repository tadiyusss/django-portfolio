from django import forms
from .models import Newsletter

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'my-2 py-2 md:mr-4 w-full px-5 border border-slate-600 bg-slate-700/20 rounded focus:outline-none focus:outline-indigo-600'})
        }

