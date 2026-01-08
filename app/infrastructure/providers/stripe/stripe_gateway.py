import stripe
import os
from app.domain.interfaces.payment_gateway import PaymentGateway
from app.application.dto.payment_request import PaymentRequest
from app.core.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


class StripeGateway(PaymentGateway):
    async def charge(self, request: PaymentRequest) -> dict:
        intent = stripe.PaymentIntent.create(
            amount=int(request.amount * 100),  # cents
            currency=request.currency.lower(),
            metadata={
                "customer_id": request.customer_id
            },
            automatic_payment_methods={"enabled": True},
        )

        return {
            "provider": "stripe",
            "payment_intent_id": intent.id,
            "client_secret": intent.client_secret,
            "status": intent.status
        }
