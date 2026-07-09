from django.db import models


class Employee(models.Model):

    DEPARTMENT_CHOICES = [
        ('IT', 'IT'),
        ('HR', 'HR'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        ('Sales', 'Sales'),
    ]

    POSITION_CHOICES = [
        ('Developer', 'Developer'),
        ('Tester', 'Tester'),
        ('HR', 'HR'),
        ('Manager', 'Manager'),
        ('UI/UX Designer', 'UI/UX Designer'),
    ]


    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=10,unique=True)

    position = models.CharField(
        max_length=30,
        choices=POSITION_CHOICES
    )

    salary = models.PositiveIntegerField()


    department = models.CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES,
    )


    joining_date = models.DateField(
        null=True,
        blank=True
    )


    location = models.CharField(
        max_length=50,
        blank=True
    )


    def __str__(self):
        return self.name