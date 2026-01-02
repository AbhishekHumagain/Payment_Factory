# Payment Service

A modular, extensible **Payment Service** built with **FastAPI** following **Clean Architecture / Hexagonal Architecture** principles. The service supports multiple payment providers (e.g., **Stripe**, **PayPal**) via a pluggable gateway system and is designed for scalability, testability, and easy provider onboarding.

---

## 🚀 Features

* ✅ FastAPI-based REST API
* ✅ Clean Architecture (Domain, Application, Infrastructure, API layers)
* ✅ Pluggable payment gateways (Stripe, PayPal)
* ✅ Central payment registry & factory
* ✅ Webhook support (Stripe)
* ✅ Strongly typed DTOs and Enums
* ✅ Dependency Injection via FastAPI `Depends`
* ✅ Ready for production & testing

---

## 🧱 Architecture Overview

```
app/
├── api/
│   └── v1/
│       ├── routes/
│       │   └── payment.py
│       └── dependencies.py
│
├── application/
│   ├── dto/
│   │   └── payment_request.py
│   └── use_cases/
│       └── process_payment.py
│
├── domain/
│   ├── enums/
│   │   └── payment_provider.py
│   └── interfaces/
│       └── payment_gateway.py
│
├── infrastructure/
│   ├── providers/
│   │   ├── stripe/
│   │   │   └── stripe_gateway.py
│   │   └── paypal/
│   │       └── paypal_gateway.py
│   ├── registry/
│   │   └── payment_registry.py
│   ├── factories/
│   │   └── payment_factory.py
│   └── webhook/
│       └── stripe_webhook.py
│
├── main.py
└── .venv/
```

---

## 🔁 Request Flow

```
Client
  ↓
FastAPI Route (/payments/{provider})
  ↓
Dependency Injection (get_payment_gateway)
  ↓
PaymentFactory → PaymentRegistry
  ↓
Concrete Gateway (Stripe / PayPal)
  ↓
process_payment Use Case
```

---

## 📦 Tech Stack

* **Python 3.11+**
* **FastAPI**
* **Uvicorn**
* **Pydantic**
* **Stripe SDK** (optional)
* **PayPal SDK** (optional)

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone <repo-url>
cd payment_service
```

### 2️⃣ Create virtual environment

```bash
python3 -m venv app/.venv
source app/.venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the server

```bash
uvicorn app.main:app --reload
```

Server will be available at:

```
http://127.0.0.1:8000
```

---

## 🩺 Health Check

```http
GET /health
```

Response:

```json
{
  "status": "ok"
}
```

---

## 💳 Create Payment API

### Endpoint

```http
POST /payments/{provider}
```

### Supported Providers

* `stripe`
* `paypal`

### Request Body

```json
{
  "amount": 100.5,
  "currency": "USD",
  "customer_id": "cust_123"
}
```

### Example

```bash
curl -X POST "http://127.0.0.1:8000/payments/stripe" \
-H "Content-Type: application/json" \
-d '{"amount":100.5,"currency":"USD","customer_id":"cust_123"}'
```

---

## 🔔 Stripe Webhook

### Endpoint

```http
POST /webhook/stripe
```

Used to handle Stripe events such as:

* payment_intent.succeeded
* payment_intent.failed

---

## 🧩 Adding a New Payment Provider

1. Create a new gateway implementing `PaymentGateway`

```python
class NewGateway(PaymentGateway):
    async def process(self, request):
        pass
```

2. Register it in `main.py`

```python
PaymentRegistry.register("new_provider", NewGateway)
```

3. Call API:

```http
POST /payments/new_provider
```

---

## 🧪 Testing

* Business logic is isolated in **use cases**
* Gateways can be mocked easily
* Ideal for unit & integration testing

---

## 👨‍💻 Author

**Abhishek Humagain**

---

## 📄 License
