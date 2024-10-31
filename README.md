Restaurant Management Application

Overview

This is a simple restaurant management application built with Flask, SQLAlchemy, and Docker. It allows you to manage a restaurant's menu and orders, including adding, updating, and viewing items and orders through a web interface.

Features

Menu Management: Add, update, and view restaurant menu items.

Order Management: Place orders, update order status, and view current orders.

User Interface: Simple web-based UI for menu and order management.

Deployment with Docker: Dockerfile and Docker Compose configuration for easy deployment.

Technologies Used

Python (Flask)

SQLAlchemy (SQLite Database)

Docker & Docker Compose

HTML, JavaScript (for front-end UI)

Getting Started

Prerequisites

Docker

Git

Clone the Repository

$ git clone https://github.com/amirali108/restaurant_app.git

$ cd restaurant_app

Run with Docker Compose

Build and start the containers:

$ docker-compose up -d --build

Access the application in your browser at:

Home Page: http://192.168.0.160:8000

View Menu: http://192.168.0.160:8000/menu

Place an Order: http://192.168.0.160:8000/order

View Orders: http://192.168.0.160:8000/view_orders

Run Locally without Docker

Create a virtual environment and activate it:

$ python3 -m venv venv

$ source venv/bin/activate

Install the required dependencies:

$ pip install -r requirements.txt

Run the Flask application:

$ python app.py

Access the application in your browser at http://192.168.0.160:8000.

Project Structure

app.py: Main application logic, including Flask routes for menu and order management.

Dockerfile: Instructions for building the Docker image.

docker-compose.yml: Configuration for deploying the application with Docker Compose.

templates/: HTML templates for the user interface.

requirements.txt: List of Python dependencies.
