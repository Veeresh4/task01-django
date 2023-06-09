# Generated by Django 4.2 on 2023-04-26 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_id', models.IntegerField(null=True)),
                ('department_name', models.CharField(choices=[('Development', 'Development'), ('Testing', 'Testing'), ('Support', 'Support'), ('Digital marketing', 'Digital marketing'), ('HR oprations', 'HR opertaions'), ('CRM', 'CRM')], default='1', max_length=100, null=True)),
                ('salaries', models.IntegerField(null=True)),
                ('task', models.CharField(max_length=100, null=True)),
                ('work_update', models.CharField(choices=[('Completed', 'Completed'), ('Incompleted', 'Incompleted')], default='1', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Manager_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_id', models.IntegerField(null=True)),
                ('manager_name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100, null=True)),
                ('employee_email', models.EmailField(max_length=254, null=True)),
                ('employee_phone', models.IntegerField(null=True)),
                ('employee_role', models.CharField(max_length=100, null=True)),
                ('employee_domain', models.CharField(max_length=100, null=True)),
                ('employee_salary', models.IntegerField(null=True)),
                ('file', models.FileField(default=None, null=True, upload_to='uploads/')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='app.department_db')),
                ('manager_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department', to='app.manager_db')),
            ],
        ),
    ]
