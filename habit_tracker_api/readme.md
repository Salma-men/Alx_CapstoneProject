
# Habit Tracker API

## Project Overview
The **Habit Tracker API** is a Django REST Framework project designed to help users track their habits, monitor progress, and maintain streaks. The API allows users to create, update, delete, and mark their habits as completed. Additional features include streak tracking, notifications, and a social component where users can follow friends and compare progress.

## Features
- **User Authentication**: Secure signup, login, and user management.
- **Habit Management**: CRUD operations for habits (create, read, update, delete).
- **Streak Tracking**: View and track habit streaks.
- **Social Features**: Follow and unfollow friends, view their progress.
- **Completion Tracking**: Mark habits as completed and incomplete.
- **Completion Rate**: View the completion rate of habits.
- **API Endpoints**: 
  - User authentication endpoints.
  - Habit CRUD and completion tracking.
  - Social features for following friends.

## Setup Instructions

### Prerequisites
Ensure that you have the following tools installed:
- Python (>= 3.8)
- Django (>= 4.0)
- Django REST Framework
- Virtual environment (optional but recommended)

### Steps to Set Up the Project

1. **Clone the Repository:**
   ```bash
   git clone <your_repo_url>
   cd <project_folder>
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the Dependencies:**
   Make sure your virtual environment is activated and then run:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations:**
   Run the following commands to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a Superuser (for accessing the admin panel):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

8. **Access the API:**
   - API documentation: `http://127.0.0.1:8000/api/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## API Endpoints

### User Authentication
- **POST** `/api/users/signup/`: Register a new user.
- **POST** `/api/users/login/`: Login and obtain a token.

### Habit Management
- **GET** `/api/habits/`: List all habits for the logged-in user.
- **POST** `/api/habits/`: Create a new habit.
- **GET** `/api/habits/{habit_id}/`: Retrieve a specific habit by ID.
- **PUT** `/api/habits/{habit_id}/`: Update a habit by ID.
- **DELETE** `/api/habits/{habit_id}/`: Delete a habit by ID.
- **POST** `/api/habits/{habit_id}/complete/`: Mark a habit as completed for today.
- **POST** `/api/habits/{habit_id}/incomplete/`: Mark a habit as incomplete for today.

### Streaks and Completion Rate
- **GET** `/api/habits/streaks/`: Get the streaks for all habits.
- **GET** `/api/habits/completion_rate/`: Get the completion rate for all habits.

### Social Features
- **POST** `/api/social/follow/`: Follow a friend.
- **POST** `/api/social/unfollow/`: Unfollow a friend.
- **GET** `/api/social/friends/`: List all friends.

## Testing the API with Postman

### 1. **Testing User Authentication**
- **POST** to `api/users/register/` with a JSON body containing:
  ```json
  {
    "username": "your_username",
    "password": "your_password",
    "email": "your_email@example.com"
  }
  ```
- **POST** to `/api/users/login/` with the same credentials to get a JWT token.

### 2. **Testing Habit CRUD**
- **GET** to `/api/habits/`: Fetch all habits.
- **POST** to `/api/habits/`: Create a new habit by sending a JSON body:
  ```json
  {
    "name": "Drink Water",
    "description": "Drink 8 glasses of water",
    "frequency": "daily"
  }
  ```
- **GET** to `/api/habits/{habit_id}/`: Retrieve a specific habit by ID.
- **PUT** to `/api/habits/{habit_id}/`: Update a habit (e.g., name or goal type).
- **DELETE** to `/api/habits/{habit_id}/`: Delete a habit by ID.

### 3. **Testing Streaks and Completion**
- **GET** to `/api/habits/streaks/`: Fetch streaks for all habits.
- **POST** to `/api/habits/{habit_id}/complete/`: Mark a habit as completed for the day.

### 4. **Testing Social Features**
- **POST** to `/api/social/follow/`: Follow a friend.
  - Example body:
    ```json
    {
      "friend_id": 2
    }
    ```
- **POST** to `/api/social/unfollow/`: Unfollow a friend.
- **GET** to `/api/social/friends/`: List all friends.

## Additional Notes
- Ensure that the user is logged in and has a valid JWT token when testing any of the protected endpoints.
- You can test the API using Postman or any other API client.

## Troubleshooting

- If you encounter errors related to migrations, try running `python manage.py makemigrations` and `python manage.py migrate` again.
- Make sure your virtual environment is activated when installing dependencies or running the project.

## License
Include your licensing information here (if applicable).

---

### Steps to Add the README File

1. In your project folder, create a new file named `README.md`.
2. Copy and paste the template above into this file.
3. Customize the sections, particularly the "API Endpoints" and "Testing with Postman" sections, to reflect any specific details related to your project.
4. Save the file.

Let me know if you need help with any part of this!