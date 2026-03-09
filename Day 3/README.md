# Course Management System (CMS)

A Django-based application for managing instructors, courses, and students. This project provides a structured way to handle educational data, including student enrollments and instructor assignments.

## Features

- **Instructor Management**: Keep track of instructors and their respective departments.
- **Course Management**: Organize courses with unique codes, descriptions, and assigned instructors.
- **Student Management**: Register students with profiles (including images) and manage their course enrollments via a Many-to-Many relationship.
- **Media Support**: Integrated `ImageField` for student profile pictures with configured media storage.

## Tech Stack

- **Framework**: [Django](https://www.djangoproject.com/)
- **Database**: SQLite (Default)
- **Language**: Python

## Project Structure

```text
Day-3/
├── cms_project/      # Project configuration (settings, URLs)
├── instructor/       # Instructor app (models, views, templates)
├── course/           # Course app (models, views, templates)
├── student/          # Student app (models, profiles, enrollments)
├── media/            # Uploaded media files (student images)
├── static/           # Static assets (CSS, JS)
├── manage.py         # Django management script
└── requirements.txt  # Project dependencies
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Day-3
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Navigate to the root URL to see the list of instructors.
- Click on an instructor to view their details and the courses they teach.
- Courses display their specific details and the students enrolled in them.
- Use the Django admin panel (`/admin/`) to manage data records easily.
