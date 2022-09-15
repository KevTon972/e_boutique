from django.urls import path

from payments.views import CreateCheckoutSessionView, paymentCancel, paymentSuccess

urlpatterns = [
    path('cancel/', paymentCancel, name='cancel'),
    path('success/', paymentSuccess, name='success'),
    path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]