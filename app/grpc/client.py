import grpc
from app.grpc import payment_pb2, payment_pb2_grpc

def test_payment():
    # Connect to gRPC server
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = payment_pb2_grpc.PaymentServiceStub(channel)

        # Create a payment request
        response = stub.ProcessPayment(
            payment_pb2.PaymentRequest(
                provider="stripe",
                amount=100.5,
                currency="USD",
                customer_id="cust_123"
            )
        )

        print("Payment status:", response.status)
        print("Transaction ID:", response.transaction_id)


if __name__ == "__main__":
    test_payment()
