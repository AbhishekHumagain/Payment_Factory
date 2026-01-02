import asyncio
from tenacity import retry, stop_after_attempt, wait_fixed
from app.domain.interfaces.payment_gateway import PaymentGateway
from app.application.dto.payment_request import PaymentRequest
from app.application.dto.payment_response import PaymentResponse

class StripeGateway(PaymentGateway):

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    async def charge(self, request: PaymentRequest) -> PaymentResponse:
        # Simulate API call
        await asyncio.sleep(0.5)
        return PaymentResponse(
            provider="stripe",
            transaction_id="txn_12345",
            status="success"
        )
