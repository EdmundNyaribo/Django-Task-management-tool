# My Django Task Management Application

This is  application is designed to create and manage tasks. 
## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)

## Features included

- User authentication and authorization
- Task creation, viewing, updating, and deletion
- Responsive design


## Installation Guide
All these should be done in the terminal
### 1. Clone the Repository:

    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name

### 2. **Create and Activate a Virtual Environment**:

    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`

### 3. **Install Dependencies**:

    Generate a requirements.txt file using this command
    
    pip freeze > requirements.txt

    Install the required packages:

    pip install -r requirements.txt

## Backend Setup

### 1. **Set Up the Database**:

    Run the following commands to create and apply database migrations:

    python manage.py makemigrations
    python manage.py migrate

### 2. **Create a Superuser**:

    Create a superuser to access the Django admin panel:

    python manage.py createsuperuser

### 3. **Run the Development Server**:

    
    python manage.py runserver
    

## Frontend Setup

If using plain HTML/CSS/JavaScript, ensure your static files are correctly placed in the `static` directory of your Django project.

## Running the Application

### 1. **Start the Backend Server**:

    python manage.py runserver

### 2. **Access the Application**:

    Backend: `http://127.0.0.1:8000`

## Usage

- **Admin Panel**: Access the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.
- **Task Management**: Use the web interface to create, edit, and delete tasks.

### Application Outlook
![Application interface](https://github.com/EdmundNyaribo/Django-Task-management-tool/blob/master/images/outlook.png)

