from fastapi import APIRouter, Request, HTTPException

router = APIRouter()

@router.post("/webhook/stripe")
async def stripe_webhook(request: Request):
    payload = await request.body()
    event_type = request.headers.get("Stripe-Event-Type", "")
    
    # Example: handle event
    if event_type == "payment_intent.succeeded":
        print("Payment succeeded")
    else:
        print("Unhandled event")
    
    return {"status": "received"}
