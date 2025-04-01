import paypalrestsdk
from decouple import config

# Initialize PayPal SDK
paypal = paypalrestsdk.Api({
    'mode': config('PAYPAL_MODE', default='sandbox'),
    'client_id': config('PAYPAL_CLIENT_ID'),
    'client_secret': config('PAYPAL_SECRET')
})

def get_paypal_client():
    return paypal