from django.urls import path
from .views import*

app_name = 'balance'

urlpatterns = [
   
    path('', home, name='home'),
    path('success/', success_view, name='payments-success'), # new
    path('cancel/', cancel_view, name='payments-cancel'), # new
    path('balance/<str:username>/', show_balance, name='show_balance'),
    path('external-page/', external_page, name='external_page'),
    path('admin-login/', admin_login_view, name='admin_login'),
    path('Contact/', Contact_view, name='Contact'),
]