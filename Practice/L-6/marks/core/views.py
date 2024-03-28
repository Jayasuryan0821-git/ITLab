from django.shortcuts import render
from .forms import Student

def student_details(request):
    # Initialize the form for GET requests
    if request.method != "POST":
        form = Student()
        return render(request, 'student_details.html', {'form': form})

    # For POST requests, process the form data
    form = Student(request.POST)
    if form.is_valid():
        total_marks = sum([form.cleaned_data[key] for key in ['marks_english', 'marks_physics', 'marks_chemistry']])
        percentage = total_marks / 3
        formatted_details = [f"{key}: {value}" for key, value in form.cleaned_data.items()]
        details = "\n".join(formatted_details)
        # You don't need 'core/templates/' if your TEMPLATES settings are configured correctly.
        return render(request, 'student_details.html', {
            'form': form,
            'details': details,
            'percentage': percentage
        })

    # If form is not valid, re-render the page with the form that includes validation errors.
    return render(request, 'student_details.html', {'form': form})
