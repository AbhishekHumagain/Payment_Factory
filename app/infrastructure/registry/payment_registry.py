from app.domain.enums.payment_provider import PaymentProvider
from app.domain.interfaces.payment_gateway import PaymentGateway

class PaymentRegistry:
    _registry = {}

    @classmethod
    def register(cls, provider_name, gateway_cls):
        cls._registry[provider_name] = gateway_cls

    @classmethod
    def get(cls, provider_name):
        # Return the gateway class, or raise an error if not registered
        if provider_name not in cls._registry:
            raise ValueError(f"Payment provider '{provider_name}' not registered")
        return cls._registry[provider_name]
