from fastapi import Depends
from app.infrastructure.registry.payment_registry import PaymentRegistry
from app.domain.enums.payment_provider import PaymentProvider
from app.domain.interfaces.payment_gateway import PaymentGateway

def get_payment_gateway(provider: PaymentProvider) -> PaymentGateway:
    return PaymentRegistry.get_provider(provider)
