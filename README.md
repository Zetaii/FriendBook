# FriendBook
![FriendBook Screenshot1](https://github.com/Zetaii/FriendBook/blob/main/friendbook2.png?raw=true)
![FriendBook Screenshot2](https://github.com/Zetaii/FriendBook/blob/main/friendbook3.png?raw=true)
![FriendBook Screenshot3](https://github.com/Zetaii/FriendBook/blob/main/friendbook1.png?raw=true)
![FriendBook Screenshot4](https://github.com/Zetaii/FriendBook/blob/main/friendbook4.png?raw=true)



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


