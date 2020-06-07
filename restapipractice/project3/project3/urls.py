"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('', views.EmployeeListCreateModelmixins.as_view()),
   # path('rud/<int:pk>', views.EmployeeRetrieveUpdateDestroyModelMixins.as_view()),
    
    
    path('api-auth/', include('rest_framework.urls')),
    path('', views.ListEmployeeAPIView.as_view()),# for displaying list of record
    path('create/',views.EmployeeCreateAPIView.as_view()), # for creating a record
    path('retrieve/<int:pk>', views.EmployeeRetrieveAPIView.as_view()), # for reterieval of specific record
    path('update/<int:pk>', views.EmployeeUpdateAPIView.as_view()),
    path('destroy/<int:pk>', views.EmployeeDestroyAPIView.as_view()),
    path('listcreate', views.EmployeeListCreateAPIView.as_view()),
    path('retrieveupdate/<int:pk>', views.EmployeeRetrieveUpdateAPIView.as_view()),
    path('retrievedestroy/<int:pk>', views.EmployeeRetrieveDestroyAPIView.as_view()),
    path('retrieveupdatedestroy/<int:pk>', views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    
    


    
]
