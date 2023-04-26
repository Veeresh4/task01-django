from django.contrib import admin
from app.models import Employee_db, Department_db, Manager_db

# Register your models here.
admin.site.register(Employee_db)
admin.site.register(Department_db)
admin.site.register(Manager_db)
