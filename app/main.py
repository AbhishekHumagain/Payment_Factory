from fastapi import FastAPI
from app.infrastructure.registry.payment_registry import PaymentRegistry
from app.infrastructure.providers.stripe.stripe_gateway import StripeGateway
from app.infrastructure.providers.paypal.paypal_gateway import PayPalGateway
from app.api.v1.routes import payment 
from app.infrastructure.webhook import stripe_webhook 


# Initialize FastAPI
app = FastAPI(title="Payment Service")
print("FastAPI app loaded:", app)

# Register Payment Providers
PaymentRegistry.register("stripe", StripeGateway)
PaymentRegistry.register("paypal", PayPalGateway)

# Include Routers
app.include_router(payment.router, prefix="/payments", tags=["payments"])
app.include_router(stripe_webhook.router, prefix="/webhook", tags=["webhook"])

# Health Check Endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}
