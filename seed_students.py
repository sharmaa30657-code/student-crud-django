import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from students.models import Student

Student.objects.all().delete()

students = [
    {"name": "Aarav Sharma", "email": "aarav.sharma@example.com", "roll_number": "CS2024001", "course": "cs", "phone": "9876543210", "status": "active"},
    {"name": "Priya Patel", "email": "priya.patel@example.com", "roll_number": "DS2024002", "course": "ds", "phone": "9876543211", "status": "active"},
    {"name": "Rohan Verma", "email": "rohan.verma@example.com", "roll_number": "IT2024003", "course": "it", "phone": "9876543212", "status": "active"},
    {"name": "Sneha Gupta", "email": "sneha.gupta@example.com", "roll_number": "AI2024004", "course": "ai", "phone": "9876543213", "status": "inactive"},
    {"name": "Kiran Mehta", "email": "kiran.mehta@example.com", "roll_number": "MCA2023005", "course": "mca", "phone": "9876543214", "status": "graduated"},
    {"name": "Arjun Singh", "email": "arjun.singh@example.com", "roll_number": "EC2024006", "course": "ec", "phone": "9876543215", "status": "active"},
]

for s in students:
    Student.objects.create(**s)

print(f"Seeded {len(students)} students.")
