from django.shortcuts import render
from app.serializers import EmployeeSerializer
from app.models import Employee
from rest_framework import generics
#from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
from app.pagination import MyPagination1, MyPagination2, MyPagination3


class EmployeeListView(generics.ListAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	#pagination_class = MyPagination # for PageNumber Pagination
	pagination_class = MyPagination2 # for limit offset pagination
	search_fields =('ename','eno')  #^eno means eno starts with , eno$ means eno ends with, =eno means exact match
	ordering_fields = ('eno','ename')# default it order by all '__all__'


	#search_fields =('^eno')
	
'''
	def get_queryset(self):
		qs = Employee.objects.all()
		name = self.request.GET.get('ename')
		if name is not None:
			qs = qs.filter(ename__icontains=name)
		return qs

'''




