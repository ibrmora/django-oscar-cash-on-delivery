# your checkout/app.py
from oscar.apps.checkout import app
from cashondelivery.views import PaymentDetailsView


class CheckoutApplication(app.CheckoutApplication):
    payment_details_view = PaymentDetailsView


application = CheckoutApplication()
