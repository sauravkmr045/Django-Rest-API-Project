from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app1.serializers import EmployeeSerializer
from app1.models import Employee
from rest_framework.authentication  import BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated #,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly 



# Create your views here.
class EmployeeBasicAuth(ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class= EmployeeSerializer

	#authentication_classes = [BasicAuthentication,]
	#permissions_classes = [IsAuthenticated,]







	#AllforAdmin
	
	


	#authentication_classes = [TokenAuthentication,]
	#permissions_classes = [IsGETOrPatch,]#AllforAdmin

	#permissions_classes = [IsReadOnly,]

	#permissions_classes = [DjangoModelPermissions,]


	#permissions_classes = [IsAuthenticated,]

	# please look at the settings.py at the end we have globally configured authentication