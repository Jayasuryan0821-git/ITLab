from django.shortcuts import render, redirect
from .models import Human
from django.http import JsonResponse

def index(request):
    if request.method == 'POST':
        if 'update' in request.POST:
            human = Human.objects.get(id=request.POST.get('human_id'))
            human.first_name = request.POST.get('first_name')
            human.last_name = request.POST.get('last_name')
            human.phone = request.POST.get('phone')
            human.address = request.POST.get('address')
            human.city = request.POST.get('city')
            human.save()
            return redirect('index')
        elif 'delete' in request.POST:
            human = Human.objects.get(id=request.POST.get('human_id'))
            human.delete()
            return redirect('index')
    
    humans = Human.objects.all()
    return render(request, 'myapp/index.html', {'humans': humans})

def get_human_details(request):
    human_id = request.GET.get('human_id')
    human = Human.objects.get(id=human_id)
    data = {
        'first_name': human.first_name,
        'last_name': human.last_name,
        'phone': human.phone,
        'address': human.address,
        'city': human.city,
    }
    return JsonResponse(data)
