from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # Calculate the percentage of marks
            total_marks = sum([form.cleaned_data[subject] for subject in ['english', 'physics', 'chemistry']])
            percentage = (total_marks / 300) * 100
            
            # Prepare content to pass to the template
            data = {
                'Name': form.cleaned_data['name'],
                'Date of Birth': form.cleaned_data['dob'].strftime("%Y-%m-%d"),  # Formatting date to string
                'Address': form.cleaned_data['address'],
                'Contact Number': form.cleaned_data['contact_number'],
                'Email': form.cleaned_data['email'],
                'Marks in English': form.cleaned_data['english'],
                'Marks in Physics': form.cleaned_data['physics'],
                'Marks in Chemistry': form.cleaned_data['chemistry'],
                'Percentage': f"{percentage:.2f}%"
            }
            
            return render(request, 'student_form.html', {'form': form, 'data': data})
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})
