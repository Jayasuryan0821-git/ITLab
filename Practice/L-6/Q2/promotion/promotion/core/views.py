from django.shortcuts import render, redirect
from .forms import Employee
from datetime import datetime
from django.http import HttpResponse

def promotion_eligibility(request):
    # Initialize an empty message
    message = None
    
    if request.method == 'POST':
        form = Employee(request.POST)
        if form.is_valid():
            date_of_joining = form.cleaned_data['date_of_joining']
            years_of_experience = (datetime.now().date() - date_of_joining).days / 365.25
            if years_of_experience > 5:
                message = 'YES'
            else:
                message = 'NO'
    else:
        form = Employee()
    
    # Ensure the view always returns an HttpResponse
    return render(request, 'promo.html', {'form': form, 'message': message})
