# FOUDARIA API

## Overview

**FOUDARIA API** is a secure and scalable RESTful API for ordering cars, designed by **Fouda Aime Emmanuel Kalvin**. This API allows users to create, manage, and view their car orders. It also provides real-time car pricing and supports authentication using JWT tokens.

### Features:
- **Authentication**: JWT-based login, signup, and token refresh.
- **Order Management**: Create, update, delete, and view car orders.
- **Car Pricing**: Fetch real-time car prices.
- **User-Specific Orders**: Each user can only view and manage their own orders.

## API Endpoints

### Authentication

- **Sign Up**: `POST /auth/signup/`
- **Login (JWT)**: `POST /auth/jwt/create/`
- **Token Refresh**: `POST /auth/jwt/refresh/`

### Order Management

- **List All Orders**: `GET /orders/`
- **View Car Prices**: `GET /orders/car-prices/`
- **Create a New Order**: `POST /orders/create/`
- **View Order Details**: `GET /orders/details/{order_id}/`
- **Delete an Order**: `DELETE /orders/delete/{order_id}/`
- **Update an Order (Full Update)**: `PUT /orders/update/{order_id}/`
- **Update an Order (Partial Update)**: `PATCH /orders/update/{order_id}/`
- **List Your Orders**: `GET /orders/my-orders/`

## Authentication

Most API endpoints require authentication using **JWT tokens**. 

### Steps for Authentication:
1. **Sign Up**: Use `/auth/signup/` to create a user account.
2. **Login**: Obtain a JWT token via `/auth/jwt/create/` with your email and password.
3. **Authorization**: To make authenticated requests, include the token in the `Authorization` header with the `Bearer` prefix (e.g., `Bearer your-access-token`).

### Token Expiry:
If your token expires, use `/auth/jwt/refresh/` to obtain a new one by providing the refresh token.

## Contact Information

For any inquiries or issues with the API, please contact:

- **Author**: Fouda Aime Emmanuel Kalvin
- **Email**: [leoemmanuelson46@gmail.com](mailto:leoemmanuelson46@gmail.com)
