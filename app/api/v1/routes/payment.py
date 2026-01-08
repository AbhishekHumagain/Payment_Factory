from fastapi import APIRouter, Depends
from app.application.dto.payment_request import PaymentRequest
from app.application.use_cases.process_payment import process_payment
from app.domain.enums.payment_provider import PaymentProvider
from app.api.v1.dependencies import get_payment_gateway

router = APIRouter()

@router.post("/{provider}")
async def create_payment(
    provider: PaymentProvider,
    request: PaymentRequest,
    gateway=Depends(get_payment_gateway)
):
    return await process_payment(provider, request)
