from django.shortcuts import render


from employee.models import Role, Designation, Employee
from leave.models import Leave


# Create your views here.


def admin_dashboard(request):
    user = request.user
    employees = Employee.objects.all()
    leaves = Leave.objects.all_pending_leaves()
    staff_leaves = Leave.objects.filter(user=user)

    context = {
        "page_title": 'Summary',
        "employees": employees,
        "leaves": leaves,
        "staff_leaves": staff_leaves,
    }
    return render(request, "admin_templates/home.html", context)
