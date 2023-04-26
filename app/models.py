from django.db import models


class Manager_db(models.Model):
    manager_id = models.IntegerField(null=True)
    manager_name = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return f"{self.manager_name}"

department_choices = (('Development', 'Development'), ('Testing', 'Testing'), ('Support', 'Support'), ('Digital marketing', 'Digital marketing'), ('HR oprations', 'HR opertaions'), ('CRM', 'CRM'))
work_status = (('Completed', 'Completed'), ('Incompleted', 'Incompleted'))


class Department_db(models.Model):  
    department_id = models.IntegerField(null=True)
    department_name = models.CharField(max_length=100, choices=department_choices, null=True, default='1')
    salaries = models.IntegerField(null=True)
    task = models.CharField(max_length=100, null=True)
    work_update = models.CharField(max_length=100, choices=work_status, null=True, default="1")

    def __str__(self) -> str:
        return f"{self.department_name}"


class Employee_db(models.Model):
    manager_name = models.ForeignKey(Manager_db, on_delete=models.CASCADE, related_name='department', null=True)
    department_name = models.ForeignKey(Department_db, on_delete=models.CASCADE, related_name='employee', null=True)

    employee_name = models.CharField(max_length=100, null=True)
    employee_email = models.EmailField(null=True)
    employee_phone = models.IntegerField(null=True)
    employee_role = models.CharField(max_length=100, null=True)
    employee_domain = models.CharField(max_length=100, null=True)
    employee_salary = models.IntegerField(null=True)
    file = models.FileField(upload_to="uploads/", max_length=100, null=True, default=None)

    def __str__(self) -> str:
        return f"{self.employee_name}"
