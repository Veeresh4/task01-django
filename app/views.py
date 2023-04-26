from django.shortcuts import render
from app.models import Employee_db, Department_db, Manager_db
from app.serializers import EmpSerializer, DepSerializer, ManagerSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import Settings
from rest_framework import filters


"""storing data"""
def register(request):
    if request.method == "POST":
        employee_name = request.POST.get("name")
        employee_email = request.POST.get("email")
        employee_phone = request.POST.get("phone")
        employee_role = request.POST.get("role")
        employee_domain = request.POST.get("domain")
        employee_salary = request.POST.get("salary")
        file = request.POST.get("file")
        obj = Employee_db.objects.create(
            employee_name=employee_name,
            employee_email=employee_email,
            employee_phone=employee_phone,
            employee_role=employee_role,
            employee_domain=employee_domain,
            employee_salary=employee_salary,
            file=file,
        )
        obj.save()
        """sending mail"""
        # send_mail(
        #     'Application status ', #subject
        #     f'Hello Mr.{employee_name} \n We are currently reviewing your application once it done. we will communicate through the email.',     # email body
        #     settings.EMAIL_HOST_USER, #sender
        #     [email], #receiver
        #     fail_silently=False,
        # )
    return render(request, "register.html")


"""generics for employee data"""
class emp_get(generics.ListCreateAPIView):
    queryset = Employee_db.objects.all()
    serializer_class = EmpSerializer
    filter_backends = [filters.SearchFilter]   # SearchFilter
    search_fields = ['employee_name', 'employee_phone', 'employee_role', 'employee_domain']


class emp_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee_db.objects.all()
    serializer_class = EmpSerializer


"""generics for department data"""
class dep_get(generics.ListCreateAPIView):
    queryset = Department_db.objects.all()
    serializer_class = DepSerializer


class dep_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department_db.objects.all()
    serializer_class = DepSerializer


"""generics for managers data"""
class manager_get(generics.ListCreateAPIView):
    queryset = Manager_db.objects.all()
    serializer_class = ManagerSerializer


class manager_update(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager_db.objects.all()
    serializer_class = ManagerSerializer   
