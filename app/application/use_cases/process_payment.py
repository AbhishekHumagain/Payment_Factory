from app.infrastructure.factories.payment_factory import PaymentFactory

async def process_payment(provider_name: str, PaymentRequest, null):
    gateway = PaymentFactory.get_gateway(provider_name)
    return await gateway.charge(PaymentRequest)