from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Employee
#from django.core.serializers import serialize
from rest_framework.renderers import JSONRenderer
from app1.serializers import EmployeeSerializer   # SERILIZER :-  OBJECT DATA ------> PYTHON DATA
from rest_framework.parsers import JSONParser	  # DESERIALIZER:- PYTHON DATA ------> OBECT DATA 
from django.views.generic import View
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



@method_decorator(csrf_exempt,name ='dispatch') # It will prevent the CSRF verification
class EmployeeCRUDCBV(View):

	def get(self,request,*args,**kwargs):
		json_data = request.body # grab the data send by the user
		stream = io.BytesIO(json_data) # convert the data into byte stream
		pdata = JSONParser().parse(stream) # Here we are converting our data to Python Dictionary
		id = pdata.get('id', None) # It will return id if dictionary has id value otherwise it will return None
		if id is not None: # If id has some value
			emp = Employee.objects.get(id =id) # get the data from database for the given id
			serializer = EmployeeSerializer(emp) # convert the database obect to to the dictionary object
			json_data = JSONRenderer().render(serializer.data) # covert the dictionary object to Json format
			return HttpResponse(json_data, content_type= 'application/json') # returnt the Json response for the given id
		qs = Employee.objects.all() #If No id was provided then fetch all the data from the database
		serializer = EmployeeSerializer(qs, many= True) #convert the all the data into python format
		json_data = JSONRenderer().render(serializer.data) # conver all the data into json format
		return HttpResponse(json_data, content_type= 'application/json') # return all the data from the database



	def post(self,request,*args,**kwargs):
		json_data = request.body # we get the data send by the application in python form
		stream = io.BytesIO(json_data) # converting the data into byte stream
		pdata = JSONParser().parse(stream) # converting the data into Json form
		serializer = EmployeeSerializer(data = pdata) # converting the data into in Dababase understandable format
		if serializer.is_valid(): # validating the data 
			serializer.validated_data
			serializer.save() # saving the data into database

			msg = {'msg': 'Resource created successfully'}# If data saved in database the send the message
			json_data = JSONRenderer().render(msg) # convert this this message into Json format
			return HttpResponse(json_data, content_type= 'application/json') #sending the message to the application

		json_data = JSONRenderer().render(serializer.errors)# get the error and convert it into json foramat
		return HttpResponse(json_data, content_type= 'application/json',status = 400) # If validation failed then send the error message



		def put(self,request,*args,**kwargs):
			json_data = request.body # we get the data send by the application in python form
			stream = io.BytesIO(json_data) # converting the data into byte stream
			pdata = JSONParser().parse(stream) # converting the data into Json form
			id = pdata.get('id')
			emp = Employee.objects.get(id =id) # get the data from database for the given id
			serializer = EmployeeSerializer(emp,data =pdata,partial = True) # convert the database obect to to the dictionary object
			if serializer.is_valid():
				serializer.save()
				msg = {'msg': 'Resource updated	 successfully'}# If data saved in database the send the message
				json_data = JSONRenderer().render(msg) # convert this this message into Json format
				return HttpResponse(json_data, content_type= 'application/json') #sending the message to the application

			json_data = JSONRenderer().render(serializer.errors)# get the error and convert it into json foramat
			return HttpResponse(json_data, content_type= 'application/json',status = 400) # If validation failed then send the error message



#----------------------------------------------------------------------------------------------------
		def delete(self,request,*args,**kwargs):
			json_data = request.body # we get the data send by the application in python form
			stream = io.BytesIO(json_data) # converting the data into byte stream
			pdata = JSONParser().parse(stream) # converting the data into Json form
			id = pdata.get('id')
			emp = Employee.objects.get(id =id) # get the data from database for the given id
			emp.delete()# Serializer concept is not required in delete operation
			msg = {'msg': 'Resource deleted successfully'}# If data saved in database the send the message
			json_data = JSONRenderer().render(msg) # convert this this message into Json format
			return HttpResponse(json_data, content_type= 'application/json') #sending the message to the application


