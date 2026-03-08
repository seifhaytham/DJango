from django.contrib import admin
from .models import Instructor


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "department")
    search_fields = ("name", "email", "department")
from django.contrib import admin

# Register your models here.
