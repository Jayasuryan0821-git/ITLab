from django.shortcuts import render
from django.http import HttpResponse
from .models import Works, Lives
from .forms import WorksForm

def index(request):
    if request.method == 'POST':
        person_name = request.POST.get('person_name')
        company_name = request.POST.get('company_name')
        salary = request.POST.get('salary')
        Works.objects.create(person_name=person_name, company_name=company_name, salary=salary)
        return HttpResponse('Data inserted successfully!')
    elif request.method == 'GET':
        company_name_query = request.GET.get('company_name_query')
        if company_name_query:
            employees = Lives.objects.filter(city=company_name_query)  # Filter by the correct field
            data = [{'person_name': employee.person_name, 'city': employee.city, 'salary': employee.salary} for employee in employees]
            return render(request, 'index.html', {'works_data': data})
        else:
            return render(request, 'index.html')


def insert_works(request):
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = WorksForm()
    return render(request, 'insert_works.html', {'form': form})

def retrieve_data(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        works_data = Works.objects.filter(company_name=company_name)  # Corrected 'Company_name' to 'company_name'
        return render(request, 'retrieve_data.html', {'works_data': works_data})
    return render(request, 'retrieve_data.html')
