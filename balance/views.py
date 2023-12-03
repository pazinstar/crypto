from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserBalance
from django.utils import timezone
from coinbase_commerce.client import Client
from django.shortcuts import render

from simple_balance_app import settings


import logging

from coinbase_commerce.client import Client
from coinbase_commerce.error import SignatureVerificationError, WebhookInvalidPayload
from coinbase_commerce.webhook import Webhook
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from simple_balance_app import settings

@csrf_exempt
@require_http_methods(['POST'])
def coinbase_webhook(request):
    import logging

    request_data = request.body.decode('utf-8')
    request_sig = request.headers.get('X-CC-Webhook-Signature', None)
    webhook_secret = settings.COINBASE_COMMERCE_WEBHOOK_SHARED_SECRET

    try:
        event = Webhook.construct_event(request_data, request_sig, webhook_secret)

        # List of all Coinbase webhook events:
        # https://commerce.coinbase.com/docs/api/#webhooks

        if event['type'] == 'charge:confirmed':
            logger.info('Payment confirmed.')
            customer_id = event['data']['metadata']['custom'] # new
            # TODO: run some custom code here
            # you can also use 'customer_id'
            # to fetch an actual Django user

    except (SignatureVerificationError, WebhookInvalidPayload) as e:
        return HttpResponse(e, status=400)

    logger.info(f'Received event: id={event.id}, type={event.type}')
    return HttpResponse('ok', status=200)















def home(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'https://cryptofinal.pythonanywhere.com/'
    product = {
        'name': 'Coffee',
        'description': 'A really good local coffee.',
         'metadata': {
        'customer_id': request.user.id if request.user.is_authenticated else None,
        'customer_username': request.user.username if request.user.is_authenticated else None,
    },
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

    
   





