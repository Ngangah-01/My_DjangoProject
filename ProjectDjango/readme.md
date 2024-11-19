Hotel Booking Management System Documentation

📋 Project Overview

The Hotel Booking Management System is a web-based platform designed to simplify and streamline the operations of hotel room management. This system enables administrators to:

Manage room information (add, edit, delete).

Approve or reject customer bookings.

Provide an intuitive and efficient interface for handling administrative tasks.

This project is built using Django, a high-level Python web framework, and incorporates Bootstrap for responsive and attractive frontend design.

Technologies Used

Backend:

Python (3.10.12): Primary programming language.

Django (5.1.3): Web framework for rapid development.

Frontend:

HTML/CSS: Core for page structure and styling.

Bootstrap: Used for creating responsive and modern UI components.

Database:

SQLite: Default database used for development and testing.
Before running the project, make sure the following are installed on your system:

Python (3.10 or higher)

Django (installation steps provided below).

A Virtual Environment setup is recommended for managing dependencies.

Steps to Run the Project

🧰 Prerequisites

Before running the project, make sure the following are installed on your system:

Python (3.10 or higher)

Django (installation steps provided below).

A Virtual Environment setup is recommended for managing dependencies.

💻 Step-by-Step Guide

Step 1️⃣: Clone the Project Repository

Open a terminal and run the following command:

git clone https://github.com//hotel_booking.git cd hotel_booking

This command downloads the project to your system and navigates to the project directory.

Step 2️⃣: Set Up a Virtual Environment (Optional but Recommended)

A virtual environment keeps project dependencies isolated. Run the following commands:

python -m venv venv # Create a virtual environment source venv/bin/activate # Activate on Linux/Mac venv\Scripts\activate # Activate on Windows

Step 3️⃣: Install Project Dependencies

Install the required Python packages using pip:

pip install -r requirements.txt

This ensures you have all the necessary libraries installed.

Step 4️⃣: Apply Database Migrations

Django requires setting up the database structure. Run:

python manage.py makemigrations python manage.py migrate

This will create the necessary tables in the database.

Step 5️⃣: Create a Superuser

To access the admin panel, you need a superuser account. Run:

python manage.py createsuperuser

Provide a username, email, and password as prompted.

Step 6️⃣: Run the Development Server

Launch the application locally using:

python manage.py runserver

Access the project by opening your browser and navigating to: http://127.0.0.1:8000/