from app.domain.enums.payment_provider import PaymentProvider
from app.domain.interfaces.payment_gateway import PaymentGateway

class PaymentRegistry:
    _registry: dict[str, type[PaymentGateway]] = {}

    @classmethod
    def register(cls, provider_name: str, gateway_cls: type[PaymentGateway]):
        cls._registry[provider_name] = gateway_cls

    @classmethod
    def get_provider(cls, provider_name: str) -> PaymentGateway:
        gateway_cls = cls._registry.get(provider_name)
        if not gateway_cls:
            raise ValueError(f"Payment provider {provider_name} not registered")
        return gateway_cls()
