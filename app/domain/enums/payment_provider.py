from enum import StrEnum

class PaymentProvider(StrEnum):
    STRIPE = "stripe"
    PAYPAL = "paypal"
