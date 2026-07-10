from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages
from django.core.paginator import Paginator


from .models import Employee


def home(request):

    employee_count = Employee.objects.count()

    department_count = Employee.objects.values('department').distinct().count()

    context = {
        'employee_count': employee_count,
        'department_count': department_count,
    }

    return render(request, 'home.html', context)
    


#🟢 LIST EMPLOYEES

@login_required
def dashboard(request):
    total_employees = Employee.objects.count()

    recent_employees = Employee.objects.order_by('-id')[:5]

    context = {
        'total_employees': total_employees,
        'recent_employees': recent_employees,
    }

    return render(request, 'dashboard.html', context)

# 🟢 LIST EMPLOYEES
@login_required
def employee_list(request):
    query = request.GET.get('q')

    employees = Employee.objects.all().order_by('-id')

    if query:
        employees = employees.filter(name__icontains=query)

    paginator = Paginator(employees, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employee_list.html', {
        'page_obj': page_obj,
        'query': query
    })

@login_required
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)

    return render(request, 'employee_detail.html', {
        'employee': employee
    })

# 🟢 ADD EMPLOYEE
@login_required
def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee added successfully!")
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})


# 🟡 EDIT EMPLOYEE
@login_required
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully!")
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'edit_employee.html', {'form': form})


# 🔴 DELETE EMPLOYEE (SAFE VERSION)
@login_required
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)

    if request.method == "POST":
        employee.delete()
        messages.success(request, "Employee deleted successfully!")
        return redirect('employee_list')

    return render(request, 'delete_confirm.html', {'employee': employee})



