# FriendBook

FriendBook is a social networking application built with Django, PostgreSQL, and Docker. The application allows users to create profiles and manage friendships.

## Features

- User registration and authentication
- Friend requests and management
- User profiles
- News feed
- Direct messaging

## Technology Stack

- **Backend**: Django + Django REST Framework
- **Database**: PostgreSQL
- **Containerization**: Docker
- **Testing**: Django Test Framework

## Getting Started

1. Clone the repository
2. Run `docker-compose up --build`
3. Access the API at `http://localhost:8000/api/`

## API Endpoints

### Authentication

- POST `/api/auth/register/` - Register new user
- POST `/api/auth/login/` - Login user
- POST `/api/auth/login/refresh/` - Refresh JWT token

### Profile

- GET/PUT `/api/auth/profile/` - Get or update user profile

### Friends

- POST `/api/friends/request/<user_id>/` - Send friend request
- PUT `/api/friends/respond/<request_id>/` - Accept/reject friend request
- GET `/api/friends/list/` - List friends

### Posts

- GET/POST `/api/posts/` - List/create posts
- GET/PUT/DELETE `/api/posts/<post_id>/` - Manage specific post

### Comments

- GET/POST `/api/posts/<post_id>/comments/` - List/create comments
- GET/PUT/DELETE `/api/posts/<post_id>/comments/<comment_id>/` - Manage specific comment
