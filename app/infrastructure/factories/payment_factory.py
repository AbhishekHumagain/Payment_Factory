from app.infrastructure.providers.stripe.stripe_gateway import StripeGateway
from app.infrastructure.providers.paypal.paypal_gateway import PayPalGateway

class PaymentFactory:
    @staticmethod
    def get_gateway(provider_name: str):
        if provider_name.lower() == "stripe":
            return StripeGateway()
        elif provider_name.lower() == "paypal":
            return PayPalGateway()
        else:
            raise ValueError(f"Unknown provider {provider_name}")
