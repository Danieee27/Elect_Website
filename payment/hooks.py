from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
import time
from .models import Order

@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    time.sleep(5)
    paypal_obj = sender
    my_invoice = str(paypal_obj.invoice)

    #match invoice to the order
    my_Order = Order.objects.get(invoice = my_invoice)

    #record payment
    my_Order.paid = True

    #save

    my_Order.save()

    #print(paypal_obj)
    #print(f'Amount Paid: {paypal_obj.mc_gross}')
