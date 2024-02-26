from django.shortcuts import render, redirect

def car_form(request):
    manufacturers = ['Toyota', 'Ford', 'Honda']
    return render(request, 'cars/car_form.html', {'manufacturers': manufacturers})

def car_details(request):
    manufacturer = request.POST.get('manufacturer')
    model_name = request.POST.get('model_name')
    return render(request, 'cars/car_details.html', {'manufacturer': manufacturer, 'model_name': model_name})
