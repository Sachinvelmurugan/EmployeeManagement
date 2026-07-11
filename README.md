# Employee Management System

A Django-based Employee Management System to manage employee records efficiently.

## Features

- Add employee details
- View employee list
- Edit employee information
- Delete employee records
- View employee details
- User login authentication
- Pagination for employee list
- Success messages
- Department and Position management

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite
- Git & GitHub

## Project Structure

```text
EmployeeManagement/
│
├── employee_management/    # Django project folder
├── employees/              # Employee management application
├── screenshots/            # Project screenshots
├── db.sqlite3              # Database file
├── manage.py               # Django management file
├── requirements.txt
└── README.md
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Sachinvelmurugan/EmployeeManagement.git
```

### 2. Go to the Project Folder

```bash
cd EmployeeManagement
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

```bash
python manage.py migrate
```

### 7. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

## Screenshots

### Dashboard

![Dashboard](screenshots/dashboard.png)

### Employee List

![Employee List](screenshots/employee_list.png)

### Add Employee

![Add Employee](screenshots/add_employee.png)

### Edit Employee

![Edit Employee](screenshots/edit_employee.png)

### Employee Details

![Employee Details](screenshots/employee_details.png)

## Author

**Sachin Velmurugan**

Python Developer | Django Developer