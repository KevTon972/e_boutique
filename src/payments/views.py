from dataclasses import replace
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
import stripe
from store.views import cart
from store.models import Cart


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):

    def post(self, request, *args, **kwargs):
        
        cart = get_object_or_404(Cart, user=request.user) 
        total = 0

        for order in cart.orders.all():
            total += order.price

        total = str(total)
        #si il n'y a qu'un seul chiffre apres la virgule rajouter un 0
        liste_total = total.split(".")

        if len(liste_total[-1]) == 1:
            total= total + "0"
        
        total = total.replace(".", "")
        total = int(total)

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'eur',
                        'unit_amount': f"{total}",
                        'product_data': {
                            'name': f"Commande n° {cart.id}",
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode = 'payment',
            success_url = settings.BASE_URL + '/payments/success/',
            cancel_url = settings.BASE_URL + '/payments/cancel/',
        )
        return redirect(checkout_session.url, code=303)

def paymentSuccess(request):
    return render(request, 'payments/success.html', context={'payment_status': 'success'})

def paymentCancel(request):
    return render(request, 'payments/cancel.html', context={'payment_status': 'cancel'})

