from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "name", "email", "gender", "image_preview")
    search_fields = ("student_id", "name", "email")
    filter_horizontal = ("courses",)

    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width='50' height='50' />")
        return "-"
    image_preview.short_description = "Image"
