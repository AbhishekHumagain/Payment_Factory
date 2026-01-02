from app.domain.interfaces.payment_gateway import PaymentGateway
from app.application.dto.payment_request import PaymentRequest
from app.application.dto.payment_response import PaymentResponse
import asyncio

class PayPalGateway(PaymentGateway):
    async def charge(self, request: PaymentRequest) -> PaymentResponse:
        # Simulate PayPal API call
        await asyncio.sleep(0.5)
        return PaymentResponse(
            provider="paypal",
            transaction_id="paypal_txn_12345",
            status="success"
        )
