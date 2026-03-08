from django.shortcuts import get_object_or_404, render
from .models import Instructor


def instructor_list(request):
    instructors = Instructor.objects.all()
    return render(request, "instructor/instructor_list.html", {"instructors": instructors})


def instructor_detail(request, pk: int):
    instructor = get_object_or_404(Instructor, pk=pk)
    courses = instructor.courses.all()
    return render(
        request,
        "instructor/instructor_detail.html",
        {"instructor": instructor, "courses": courses},
    )
