from pydantic import BaseModel

class PaymentResponse(BaseModel):
    provider: str
    transaction_id: str
    status: str
