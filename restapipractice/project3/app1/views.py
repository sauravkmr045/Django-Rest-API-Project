from django.shortcuts import render
from rest_framework.views import APIView
from app1.models import Employee
from app1.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.generics import UpdateAPIView,DestroyAPIView,ListCreateAPIView, RetrieveUpdateAPIView

'''class ListEmployeeAPIView(APIView):
	def get(self,request,format =None):
		qs = Employee.objects.all()
		serializer = EmployeeSerializer(qs, many = True)
		return Response(serializer.data)  '''
#----------------------------------------------------------------------------------------------------------------
#MIXINS VIEW CONCEPT


#	from rest_framework import generics
'''from rest_framework import mixins
class EmployeeListCreateModelmixins(mixins.CreateModelMixin,ListAPIView):  
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

	def post(self,request,*args,**kwargs):  # HERE WE ARE USING MIXIN CLASS
		return self.create(request,*args,**kwargs)


class EmployeeRetrieveUpdateDestroyModelMixins(mixins.UpdateModelMixin,mixins.DestroyModelMixin,RetrieveAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def patch(self,request,*args,**kwargs):
		return self.partial_update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)

		'''

#-------------------------------------------------------------------------------------------------------



class ListEmployeeAPIView(ListAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
# for overriding the search operation we implement get_queryset(self)
	def get_queryset(self):
		qs = Employee.objects.all()
		name = self.request.GET.get('ename')
		if name is not None:
			qs = qs.filter(ename__icontains= name)
		return qs

class EmployeeCreateAPIView(CreateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class EmployeeRetrieveAPIView(RetrieveAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	#lookup_field ='id'  If we want to look up with any other field than pk then we use this lookup field in urls.py

class EmployeeUpdateAPIView(UpdateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class EmployeeDestroyAPIView(DestroyAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class EmployeeListCreateAPIView(ListCreateAPIView): # used for creating and listing the record simultaneously
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer



class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView): #
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer
	#lookup_field = 'id'

	