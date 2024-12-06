# Flask Leaderboard App

This is a Flask application for leaderboard management with MongoDB integration, QR code generation, and background jobs.

## [Backend API URL](https://spring-flask.vercel.app/)


## Prerequisites

- Python 3.10+
- MongoDB
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your MongoDB credentials:
   ```
   MONGO_USERNAME=your_username
   MONGO_PASSWORD=your_password
   ```

## Running the Application

To run the Flask application:

```
python wsgi.py
```


## Flask CLI Commands

This application includes custom Flask CLI commands:

1. Reset all user scores to 0:
   ```
   flask reset-scores
   ```

2. Seed the database with random users:
   ```
   flask seed-db --count 10
   ```
   (Replace 10 with the desired number of users)

## API Endpoints

- GET `/`: Index route
- GET `/users`: Get all users
  - Query parameters:
    - `sort_by`: Field to sort by (default: "points")
    - `order`: Sort order (-1 for descending, 1 for ascending, default: -1)
    - `search`: Search users by name
- GET `/users/<user_id>`: Get a specific user
- POST `/users`: Add a new user
- DELETE `/users/<user_id>`: Delete a user
- PATCH `/users/<user_id>/points`: Update user points
- GET `/users/grouped`: Get users grouped by points
- POST `/users/qr`: Generate QR code for a user
- GET `/uploads/<filename>`: Retrieve a generated QR code image

## Background Jobs

The application includes background jobs for:
- Listening to MongoDB change streams
- Selecting winners based on user points

These jobs run automatically when the Flask application starts.
