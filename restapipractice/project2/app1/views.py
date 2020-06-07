from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from app1.serializers import NameSerializer

# Create your views here.

class TestAPIView(APIView):
	def get(self, request,*args,**kwargs):
		colors = ['RED', 'BLUE', 'GREEN','WHITE']
		# here response class is responsible for converting the data to JSON 
		return Response({'msg':'I m learning APIView','colors': colors})


	def post(self, request,*args, **kwargs):
		data = request.data # We have to request.data 
		serializer = NameSerializer(data=data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			msg = 'Hi {} great to see u doing programming'.format(name)
			return Response({'msg':msg})
		else:
			return Response(serializer.errors,status = 400)

	def put(self,request,*args,**kwargs):
		return Response({'msg':' This response is coming from put method'})

	def patch(self,request,*args,**kwargs):
		return Response({'msg':' This response is coming from patch	 method'})


	def delete(self,request,*args,**kwargs):
		return Response({'msg':' This response is coming from delete method'})

#===============================================================================================================
from rest_framework.viewsets import ViewSet
class TestViewSet(ViewSet):
	def list(self, request,*args,**kwargs):
		colors = ['RED', 'BLUE', 'GREEN','WHITE']
		# here response class is responsible for converting the data to JSON 
		return Response({'msg':'I m learning APIView','colors': colors})


	def create(self, request,*args, **kwargs):
		data = request.data # We have to request.data 
		serializer = NameSerializer(data=data)
		if serializer.is_valid():
			name = serializer.data.get('name')
			msg = 'Hi {} great to see u doing programming'.format(name)
			return Response({'msg':msg})
		else:
			return Response(serializer.errors,status = 400)


	def retrieve(self,request,pk= None):
		return Response({'msg':' This response is coming from create method'})


	def partial_update(self,request,pk= None):
		return Response({'msg':' This response is coming from partial_update method'})

	def destroy(self,request,pk= None):
		return Response({'msg':' This response is coming from destroy method'})

	def update(self,request,pk= None):
		return Response({'msg':' This response is coming from update method'})








































