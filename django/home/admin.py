from django.contrib import admin
from .models import Foods


class PostAdmin(admin.ModelAdmin):
    verbose_name = 'Food'
    list_display = ('title', 'content')

# Register your models here.
admin.site.register(Foods, PostAdmin)