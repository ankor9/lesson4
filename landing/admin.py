from django.contrib import admin
from landing.models import *
# Register your models here.

@admin.register(EmailCollector)
class EmailCollectorAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'email',
        'time_create'
    ]

#admin.site.register(EmailCollector, EmailCollectorAdmin) same as @admin.register(EmailCollector)
