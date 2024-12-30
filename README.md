# FriendBook

FriendBook is a social networking application built with Django, PostgreSQL, and Docker. The application allows users to create profiles and manage friendships.

## Features

- User registration and authentication
- User profiles

## Technology Stack

- **Backend**: Django +
- **Database**: PostgreSQL
- **Containerization**: Docker

## Getting Started

1. Clone the repository
2. Run `docker-compose up --build`
3. Access the API at `http://localhost:8000/api/`

## API Endpoints

### Authentication

- POST `/api/auth/register/` - Register new user
- POST `/api/auth/login/` - Login user

### Profile

- GET/PUT `/api/auth/profile/` - Get or update user profile


