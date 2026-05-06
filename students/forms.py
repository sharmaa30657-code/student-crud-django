from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'roll_number', 'course', 'phone', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full name...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'student@email.com'}),
            'roll_number': forms.TextInput(attrs={'placeholder': 'e.g. CS2024001'}),
            'phone': forms.TextInput(attrs={'placeholder': '+91 9876543210'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = Student.objects.filter(email=email)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("A student with this email already exists.")
        return email

    def clean_roll_number(self):
        roll = self.cleaned_data.get('roll_number')
        qs = Student.objects.filter(roll_number=roll)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This roll number is already taken.")
        return roll
