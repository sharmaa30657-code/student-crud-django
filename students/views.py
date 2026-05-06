from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Student
from .forms import StudentForm


def student_list(request):
    query = request.GET.get('q', '')
    course = request.GET.get('course', '')
    status = request.GET.get('status', '')

    students = Student.objects.all()
    if query:
        students = students.filter(
            Q(name__icontains=query) | Q(email__icontains=query) | Q(roll_number__icontains=query)
        )
    if course:
        students = students.filter(course=course)
    if status:
        students = students.filter(status=status)

    context = {
        'students': students,
        'query': query,
        'selected_course': course,
        'selected_status': status,
        'course_choices': Student.COURSE_CHOICES,
        'status_choices': Student.STATUS_CHOICES,
        'total': students.count(),
    }
    return render(request, 'students/student_list.html', context)


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'Student "{student.name}" added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'action': 'Add Student'})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, f'"{student.name}" updated successfully!')
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'student': student, 'action': 'Edit Student'})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        name = student.name
        student.delete()
        messages.success(request, f'Student "{name}" has been deleted.')
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
