# views.py

from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        # Process form submission
        # Retrieve form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact_number = request.POST.get('contact_number')
        # Render success page with data
        return render(request, 'registration/success.html', {'username': username, 'email': email, 'contact_number': contact_number})
    return render(request, 'registration/register.html')

def generate_bill(request):
    if request.method == 'POST':
        # Process form submission
        # Retrieve form data
        brand = request.POST.get('brand')
        category = request.POST.getlist('category')
        quantity = int(request.POST.get('quantity', 0))
        # Calculate total amount based on selected items and quantity (dummy calculation)
        total_amount = 100 * quantity  # Assuming $100 per item
        # Render bill page with data
        return render(request, 'registration/bill_page.html', {'brand': brand, 'category': ', '.join(category), 'quantity': quantity, 'total_amount': total_amount})
    # Redirect to the first page if accessed directly without form submission
    return render(request, 'registration/first_page.html')
