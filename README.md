# 🛒 Ecommerce Microservices  

This project is a **microservices-based e-commerce system** built using **Django REST Framework (DRF)** and **FastAPI**, with support for asynchronous tasks and containerized deployment.  

---

## 📌 Project Structure & Features  

```bash
ecommerce-microservices/
│── user_service/          # User authentication & management (DRF)
│── product_service/       # Product catalog & details (FastAPI)
│── order_service/         # Order management (DRF)
│── payment_service/       # Payment processing (FastAPI)
│── inventory_service/     # Inventory tracking (DRF or FastAPI)
│── notification_service/  # Email/SMS/Push notifications (FastAPI + Celery + Redis)
│── api_gateway/           # API Gateway (FastAPI)
│── docker-compose.yml     # DB, Redis, RabbitMQ, and services setup
│── README.md

---
## 🚀 Features  

### 👤 User Service
- User registration, login, logout, and profile management
- JWT authentication and role-based access control
- Password reset and email verification
- User activity tracking

### 📦 Product Service
- Add, update, delete, and list products
- Categorization and product search
- Product detail view with images and specifications
- Support for product variants (size, color, etc.)

### 🛒 Order Service
- Add items to cart and manage cart
- Checkout and order placement
- Order history and status tracking
- Cancel or return orders

### 💳 Payment Service
- Secure payment processing
- Integration with multiple payment gateways
- Transaction history and receipts
- Refund and payment status updates

### 📊 Inventory Service
- Track stock levels in real-time
- Automatic stock updates on order placement
- Low-stock alerts and notifications
- Support for multiple warehouses or locations

### 🔔 Notification Service
- Send email, SMS, and push notifications
- Background task processing with Celery
- Notification templates for different events
- Retry mechanism for failed deliveries

### 🌍 API Gateway
- Centralized entry point for all microservices
- Request routing to appropriate services
- Load balancing support
- Authentication and rate limiting

