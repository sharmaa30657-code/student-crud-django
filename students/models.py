from django.db import models


class Student(models.Model):
    COURSE_CHOICES = [
        ('cs', 'Computer Science'),
        ('it', 'Information Technology'),
        ('ds', 'Data Science'),
        ('ai', 'Artificial Intelligence'),
        ('ec', 'Electronics & Communication'),
        ('me', 'Mechanical Engineering'),
        ('ce', 'Civil Engineering'),
        ('ba', 'Business Administration'),
        ('bca', 'BCA'),
        ('mca', 'MCA'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('graduated', 'Graduated'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    course = models.CharField(max_length=10, choices=COURSE_CHOICES)
    phone = models.CharField(max_length=15, blank=True)
    roll_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.roll_number})"
