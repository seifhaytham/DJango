from django.shortcuts import get_object_or_404, render
from .models import Course


def course_detail(request, pk: int):
    course = get_object_or_404(Course, pk=pk)
    students = course.students.all()
    return render(
        request,
        "course/course_detail.html",
        {"course": course, "students": students},
    )
