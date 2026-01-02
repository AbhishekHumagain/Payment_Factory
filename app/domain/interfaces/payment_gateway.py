from abc import ABC, abstractmethod
from app.application.dto.payment_request import PaymentRequest
from app.application.dto.payment_response import PaymentResponse

class PaymentGateway(ABC):

    @abstractmethod
    async def charge(self, request: PaymentRequest) -> PaymentResponse:
        pass
