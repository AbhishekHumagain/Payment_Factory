from concurrent import futures
import grpc
import asyncio

from app.grpc import payment_pb2, payment_pb2_grpc
from app.application.dto.payment_request import PaymentRequest
from app.application.use_cases.process_payment import process_payment
from app.infrastructure.registry.payment_registry import PaymentRegistry
from app.domain.enums.payment_provider import PaymentProvider
from app.infrastructure.providers.stripe.stripe_gateway import StripeGateway
from app.infrastructure.providers.paypal.paypal_gateway import PayPalGateway


class PaymentService(payment_pb2_grpc.PaymentServiceServicer):
    async def _process(self, request):
        provider = PaymentProvider(request.provider)
        gateway_cls = PaymentRegistry.get(provider.value)
        gateway = gateway_cls()

        payment_request = PaymentRequest(
            amount=request.amount,
            currency=request.currency,
            customer_id=request.customer_id
        )

        result = await process_payment(provider, payment_request, gateway)

        return payment_pb2.PaymentResponse(
            status=result.get("status", "unknown"),
            transaction_id=result.get("payment_intent_id", "")
        )

    def ProcessPayment(self, request, context):
        return asyncio.run(self._process(request))

PaymentRegistry.register("stripe", StripeGateway)
PaymentRegistry.register("paypal", PayPalGateway)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    payment_pb2_grpc.add_PaymentServiceServicer_to_server(
        PaymentService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("✅ gRPC server running on port 50051")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
