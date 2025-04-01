"""
URL configuration for foudaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="FOUDARIA API",
        default_version="v1",
        description=(
            "# DOCUMENTATION\n\n"
            "## Overview\n"
            "FOUDARIA API is a secure and scalable RESTful API for ordering cars, designed by **Fouda Aime Emmanuel Kalvin**. "
            "It provides authentication, order management, and car pricing services for a seamless user experience.\n\n"
            "### Base URL:\n"
            "```\nhttp://127.0.0.1:8000/\n```\n\n"
            "## Authentication\n"
            "All API endpoints **require authentication** using **JWT tokens**, except for `signup` and `login`. Follow these steps to authenticate:\n\n"
            "1. **Sign Up:** Create an account using `/auth/signup/`.\n"
            "2. **Log In:** Obtain a JWT token via `/auth/jwt/create/` by providing your email and password.\n"
            "3. **Authorize Requests:**\n"
            "   - Click on the **'Authorize'** button in Swagger UI.\n"
            "   - Enter your token in this format: `Bearer your-access-token-here`.\n"
            "   - Click **Authorize** to start making authenticated requests.\n"
            "4. **Token Refresh:** If your access token expires, use `/auth/jwt/refresh/` to obtain a new one.\n\n"
            "## Authentication Endpoints\n"
            "### Register a New User\n"
            "**POST** `/auth/signup/`\n"
            "#### Request Body:\n"
            "```json\n{\n  \"username\": \"string\",\n  \"email\": \"user@example.com\",\n  \"phone_number\": \"string\",\n  \"password\": \"stringst\"\n}\n```\n"
            "#### Response:\n- **201 Created**: Account successfully created.\n- **400 Bad Request**: Invalid data.\n\n"
            "### Log In (Obtain JWT Token)\n"
            "**POST** `/auth/jwt/create/`\n"
            "#### Request Body:\n"
            "```json\n{\n  \"email\": \"string\",\n  \"password\": \"string\"\n}\n```\n"
            "#### Response:\n"
            "```json\n{\n  \"refresh\": \"your-refresh-token\",\n  \"access\": \"your-access-token\"\n}\n```\n\n"
            "### Refresh JWT Token\n"
            "**POST** `/auth/jwt/refresh/`\n"
            "#### Request Body:\n"
            "```json\n{\n  \"refresh\": \"your-refresh-token\"\n}\n```\n"
            "#### Response:\n"
            "```json\n{\n  \"access\": \"your-new-access-token\"\n}\n```\n\n"
            "---\n\n"
            "## Order Management\n"
            "### List All Orders\n"
            "**GET** `/orders/`\n"
            "#### Response:\n"
            "- **200 OK**: Returns a list of all orders.\n"
            "```json\n[\n  {\n    \"customer\": \"John Doe\",\n    \"order_id\": \"123e4567-e89b-12d3-a456-426614174000\",\n    \"car\": \"Toyota Camry\",\n    \"quantity\": 1,\n    \"price\": \"30000.00\",\n    \"order_status\": \"Pending\",\n    \"payment_status\": \"Paid\",\n    \"payment_method\": \"PayPal\",\n    \"created_at\": \"2025-04-01T12:34:56Z\",\n    \"updated_at\": \"2025-04-01T12:34:56Z\"\n  }\n]\n```\n\n"
            "### View Car Prices\n"
            "**GET** `/orders/car-prices/`\n"
            "#### Response:\n"
            "- **200 OK**: Returns available cars and their prices.\n"
            "```json\n[\n  {\n    \"car\": \"Toyota Camry\",\n    \"price\": \"30000.00\"\n  }\n]\n```\n\n"
            "### Create a New Order\n"
            "**POST** `/orders/create/`\n"
            "#### Request Body:\n"
            "```json\n{\n  \"car\": \"Toyota Camry\",\n  \"quantity\": 1,\n  \"payment_method\": \"PayPal\"\n}\n```\n"
            "#### Response:\n- **201 Created**: Order successfully created.\n"
            "```json\n{\n  \"customer\": \"John Doe\",\n  \"order_id\": \"123e4567-e89b-12d3-a456-426614174000\",\n  \"car\": \"Toyota Camry\",\n  \"quantity\": 1,\n  \"price\": \"30000.00\",\n  \"order_status\": \"Pending\",\n  \"payment_status\": \"Paid\",\n  \"payment_method\": \"PayPal\",\n  \"created_at\": \"2025-04-01T12:34:56Z\",\n  \"updated_at\": \"2025-04-01T12:34:56Z\"\n}\n```\n\n"
            "### View Order Details\n"
            "**GET** `/orders/details/{order_id}/`\n"
            "#### Response:\n"
            "- **200 OK**: Returns order details.\n\n"
            "### Delete an Order\n"
            "**DELETE** `/orders/delete/{order_id}/`\n"
            "#### Response:\n- **204 No Content**: Order successfully deleted.\n\n"
            "### Update an Order (Full Update)\n"
            "**PUT** `/orders/update/{order_id}/`\n"
            "#### Request Body:\n"
            "```json\n{\n  \"car\": \"Honda Civic\",\n  \"quantity\": 2,\n  \"payment_method\": \"Stripe\"\n}\n```\n"
            "#### Response:\n- **200 OK**: Order successfully updated.\n\n"
            "### Update an Order (Partial Update)\n"
            "**PATCH** `/orders/update/{order_id}/`\n"
            "#### Request Body:\n"
            "```json\n{\n  \"quantity\": 2\n}\n```\n"
            "#### Response:\n- **200 OK**: Order successfully updated.\n\n"
            "### List Your Own Orders\n"
            "**GET** `/orders/my-orders/`\n"
            "#### Response:\n- **200 OK**: Returns orders belonging to the authenticated user.\n\n"
            "---\n\n"
            "## Error Handling\n"
            "The API returns the following error responses:\n"
            "- **400 Bad Request**: Invalid input data.\n"
            "- **401 Unauthorized**: Invalid or missing authentication token.\n"
            "- **403 Forbidden**: You do not have permission to access this resource.\n"
            "- **404 Not Found**: Requested resource does not exist.\n"
            "- **500 Internal Server Error**: An unexpected error occurred on the server.\n\n"
            "---\n\n"
            "## Contact Information\n"
            "📧 Email: [leoemmanuelson46@gmail.com](mailto:leoemmanuelson46@gmail.com)\n"
            "👤 Author: Fouda Aime Emmanuel Kalvin"
        ),
        contact=openapi.Contact(
            name="Fouda Aime Emmanuel Kalvin",
            email="leoemmanuelson46@gmail.com",
        ),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-ui'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('orders/', include('orders.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('doc/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
