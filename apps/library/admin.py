from django.contrib import admin

# Register your models here.
from apps.library.models import Library

admin.site.register(Library)