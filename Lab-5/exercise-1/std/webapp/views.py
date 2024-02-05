from django.shortcuts import render
from .forms import StudentForm

def student_form_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            total_marks = student.marks_english + student.marks_physics + student.marks_chemistry
            percentage = (total_marks / 300) * 100
            form = StudentForm()
            return render(request, 'student_form.html', {'form': form, 'student': student, 'percentage': percentage})
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
