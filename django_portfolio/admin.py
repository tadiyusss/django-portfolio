from django.contrib import admin
from .models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added', 'newsletter_id')
    search_fields = ('email', 'date_added', 'newsletter_id')

    
admin.site.register(Newsletter, NewsletterAdmin)