"""project2 URL Configuration

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

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
#router.register('api' ,views.EmployeeCRUBCBV, basename='api')  # router.register('anyname',views.classname,basename='anyname')
router.register('api' ,views.EmployeeCRUBCBV) # we can remove basename for ModelViewset, first parameter could have anyname
#from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token
urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include(router.urls)),
   #path('token/', views.obtain_auth_token, name= 'token'),
   path('auth-jwt/', obtain_jwt_token),
   path('auth-jwt-refresh/',refresh_jwt_token),
   path('auth-jwt-verify/', verify_jwt_token)
]


#http://127.0.0.1:8000/api/ "authorization : Token d4a7932bb7274a29609f510e1d9d1e7558485ee2"

#http://127.0.0.1:8000/token/ username = "admin" password = "admin"
