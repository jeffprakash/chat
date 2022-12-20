from django.urls import path ,include
from rest_framework import routers
#from . import UserViewSet
from . import views
 #router=routers.DefaultRouter()
#router.register('api/users',LeadViewSet)
urlpatterns = [
    path("get-info/",views.get_list, name="get-info1-list"),
    path("add-info/",views.addinfo.as_view(), name="add-info1-list"),
   
   
    
   
]
 