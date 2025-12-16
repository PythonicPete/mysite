# 🚀 Django OnePage Portfolio

A modern, full-stack portfolio website built with **Django (Python)**. This project integrates a responsive HTML5 template with a robust Django backend to handle user data and dynamic content.

## 🌟 Key Features
* **User Authentication:** Secure Signup, Login, and Logout functionality.
* **Dynamic Contact Form:** Messages sent from the frontend are saved directly to the database.
* **Responsive Design:** Fully optimized for mobile and desktop using a custom "OnePage" template.
* **Admin Dashboard:** easy management of users and contact messages.
* **Static Files Management:** Organized handling of CSS, JavaScript, and Images.

## 🛠️ Tech Stack
* **Backend:** Python, Django
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap (OnePage Template)
* **Database:** SQLite (Default)

## ⚙️ How to Run Locally

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git)
    cd YourRepoName
    ```

2.  **Install Django** (if not installed)
    ```bash
    pip install django
    ```

3.  **Apply Migrations** (Create the database)
    ```bash
    python manage.py migrate
    ```

4.  **Create a Superuser** (To access the Admin panel)
    ```bash
    python manage.py createsuperuser
    ```

5.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

## 📂 Project Structure
* `mysite/` - Main project configuration.
* `iapp/` - Main application logic (Views, Models).
* `static/` - CSS, JS, and Images assets.
* `templates/` - HTML files (index.html, signup.html, etc.).

---
*Created by Gourav*
