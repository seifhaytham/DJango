from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Seed the database with sample instructors, courses, and students."

    def handle(self, *args, **options):
        from instructor.models import Instructor
        from course.models import Course
        from student.models import Student

        # Instructors
        alice, _ = Instructor.objects.get_or_create(
            email="alice.smith@example.com",
            defaults={"name": "Dr. Alice Smith", "department": "Computer Science"},
        )
        bob, _ = Instructor.objects.get_or_create(
            email="bob.johnson@example.com",
            defaults={"name": "Prof. Bob Johnson", "department": "Mathematics"},
        )
        carol, _ = Instructor.objects.get_or_create(
            email="carol.lee@example.com",
            defaults={"name": "Dr. Carol Lee", "department": "Physics"},
        )

        # Courses
        cs101, _ = Course.objects.get_or_create(
            code="CS101",
            defaults={
                "title": "Introduction to Programming",
                "description": "Learn the basics of programming with Python.",
                "instructor": alice,
            },
        )
        cs201, _ = Course.objects.get_or_create(
            code="CS201",
            defaults={
                "title": "Data Structures",
                "description": "Study fundamental data structures and algorithms.",
                "instructor": alice,
            },
        )
        ma101, _ = Course.objects.get_or_create(
            code="MA101",
            defaults={
                "title": "Calculus I",
                "description": "Differential and integral calculus of one variable.",
                "instructor": bob,
            },
        )
        ph101, _ = Course.objects.get_or_create(
            code="PH101",
            defaults={
                "title": "Classical Mechanics",
                "description": "Newtonian mechanics and applications.",
                "instructor": carol,
            },
        )

        # Students
        s1, _ = Student.objects.get_or_create(
            student_id="S1001",
            defaults={
                "name": "John Doe",
                "email": "john.doe@example.com",
                "gender": "M",
            },
        )
        s2, _ = Student.objects.get_or_create(
            student_id="S1002",
            defaults={
                "name": "Jane Miller",
                "email": "jane.miller@example.com",
                "gender": "F",
            },
        )
        s3, _ = Student.objects.get_or_create(
            student_id="S1003",
            defaults={
                "name": "Carlos Ruiz",
                "email": "carlos.ruiz@example.com",
                "gender": "M",
            },
        )
        s4, _ = Student.objects.get_or_create(
            student_id="S1004",
            defaults={
                "name": "Amina Khan",
                "email": "amina.khan@example.com",
                "gender": "F",
            },
        )

        # Enrollments (many-to-many)
        s1.courses.set([cs101, ma101])
        s2.courses.set([cs101, cs201, ph101])
        s3.courses.set([ma101, ph101])
        s4.courses.set([cs201])

        self.stdout.write(self.style.SUCCESS("Sample instructors, courses, and students have been created/updated."))

