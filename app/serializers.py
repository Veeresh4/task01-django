from contextlib import nullcontext
from rest_framework import serializers
from app.models import Employee_db, Department_db, Manager_db


class EmpSerializer(serializers.ModelSerializer):
    manager_name = serializers.SerializerMethodField(source='get_manager_name')
    department_name = serializers.SerializerMethodField(source='get_department_name')

    class Meta:
        model = Employee_db
        fields = "__all__"

    def get_manager_name(self, obj):
        display = str(obj.manager_name)
        return display

    def get_department_name(self, obj):
        display = str(obj.department_name)
        return display

    """object level validation"""
    def validate(self, data):
        if len(data['employee_name']) <= 3:
            raise serializers.ValidationError("You have to take more than 3 characters")
        # elif Employee_db.objects.filter(employee_email=data['employee_email']).exists():
        #     raise serializers.ValidationError("email alredy existed")
        elif data['employee_email'] == nullcontext:
            raise serializers.ValidationError("dont leave the email field empty")
        elif data['employee_role'] == int:
            raise serializers.ValidationError("dont use int values")
        else:
            return data


class DepSerializer(serializers.ModelSerializer):
    employee = EmpSerializer(many=True, read_only=True)
    class Meta:
        model = Department_db
        fields = "__all__"


class ManagerSerializer(serializers.ModelSerializer):
    department = DepSerializer(many=True, read_only=True)
    class Meta:
        model = Manager_db
        fields = "__all__"
