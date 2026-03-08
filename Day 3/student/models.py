from django.db import models
from course.models import Course


class Student(models.Model):
    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
    image = models.ImageField(upload_to="student_images/", blank=True, null=True)
    courses = models.ManyToManyField(Course, related_name="students", blank=True)

    class Meta:
        ordering = ["student_id"]

    def __str__(self) -> str:
        return f"{self.student_id} - {self.name}"
