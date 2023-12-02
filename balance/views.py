from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserBalance
from django.utils import timezone
from coinbase_commerce.client import Client
from django.shortcuts import render

from simple_balance_app import settings

def home(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'http://localhost:8000/'
    product = {
        'name': 'Coffee',
        'description': 'A really good local coffee.',
        'local_price': {
            'amount': '.10',
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
    }
    charge = client.charge.create(**product)

    return render(request, 'balance/home.html', {
        'charge': charge,
    })





    if request.method == 'POST':
        username = request.POST.get('username')
    
        user = UserBalance.objects.filter(username=username).first()
       
        if user:
            return redirect('balance:show_balance', username=username)
        else:
            messages.error(request, 'User does not exist. Contact admin.')
    return render(request, 'balance/home.html')
def success_view(request):
    return render(request, 'balance/success.html', {})


def cancel_view(request):
    return render(request, 'balance/cancel.html', {})









def show_balance(request, username):
    user = UserBalance.objects.get(username=username)
    return render(request, 'balance/show_balance.html', {'user': user})
def Contact_view(request):
    
    return render(request, 'balance/contact.html')

def external_page(request):
    # Replace 'https://www.example.com' with the actual external link you want to display
    external_url = 'https://kdc2.000webhostapp.com/index.php'
    return render(request, 'balance/external_page.html', {'external_url': external_url})
from django.shortcuts import redirect

from django.shortcuts import redirect

def admin_login_view(request):
    # Redirect to the admin login page
    return redirect('admin:login')

    
   





