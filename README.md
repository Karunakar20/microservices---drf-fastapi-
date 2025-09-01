# microservices - (drf + fastapi)

ecommerce-microservices/
│── user_service/          # Django + DRF
│── product_service/       # FastAPI
│── order_service/         # Django + DRF
│── payment_service/       # FastAPI
│── inventory_service/     # FastAPI or DRF
│── notification_service/  # FastAPI + Celery
│── api_gateway/           # FastAPI
│── docker-compose.yml     # DB + Redis + all services
│── README.md
