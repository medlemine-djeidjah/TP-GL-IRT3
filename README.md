# 🚗 Roadside Assistance App

Welcome to the Roadside Assistance App! This project is designed to provide timely and effective roadside assistance services through a Django-powered web application. 

## 📋 Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)

## ✨ Features
- **User Registration & Authentication**: Secure user registration and login.
- **Service Requests**: Users can request assistance for various roadside issues.
- **Real-time Updates**: Track the status of service requests in real-time.
- **Admin Dashboard**: Admins can manage service requests and users.
- **Notifications**: Email notifications for service request updates.

## 🛠️ Installation
To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/roadside-assistance-app.git
    cd roadside-assistance-app
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

    Access the app at `http://127.0.0.1:8000/`.

## 🚀 Usage
1. **Register an account**: Users can sign up and log in.
2. **Request Assistance**: Create a new service request specifying the issue.
3. **Track Requests**: Monitor the status of your service requests.
4. **Admin Management**: Admins can log in to manage requests and users.

## 👥 Contributors
This project was developed by:
- [23244](mailto:23244@esp.mr)
- [23009](mailto:23009@esp.mr)
- [23043](mailto:23043@esp.mr)
- [23059](mailto:23059@esp.mr)

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
