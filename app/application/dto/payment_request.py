from pydantic import BaseModel

class PaymentRequest(BaseModel):
    amount: float
    currency: str
    customer_id: str
