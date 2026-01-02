from proto import payment_pb2, payment_pb2_grpc
from app.application.use_cases.process_payment import process_payment
from app.domain.enums.payment_provider import PaymentProvider

class PaymentService(payment_pb2_grpc.PaymentServiceServicer):

    async def Charge(self, request, context):
        response = await process_payment(
            PaymentProvider(request.provider),
            request
        )
        return payment_pb2.PaymentResponse(
            transaction_id=response.transaction_id,
            status=response.status
        )
