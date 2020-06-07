from django.contrib import admin
from app1.models import Employee
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
	model = Employee
	list_display = ['id','ename','eno','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)