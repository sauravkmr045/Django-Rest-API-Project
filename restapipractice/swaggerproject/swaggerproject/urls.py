
from django.contrib import admin
from django.urls import path,include
from app1 import views 
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title = 'Swagger API Testing by using Swagger')
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('api' ,views.EmployeeBasicAuth)


 # we can remove basename for ModelViewset, first parameter could have anyname
urlpatterns = [
    path('admin/', admin.site.urls),
   path('', include(router.urls)),
   path('accounts/',include('django.contrib.auth.urls')),
   path('docs/',schema_view)

]


#http://127.0.0.1:8000/api/ "authorization : Token d4a7932bb7274a29609f510e1d9d1e7558485ee2"

#http://127.0.0.1:8000/token/ username = "admin" password = "admin"
