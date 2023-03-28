from django.urls import path, include
from . import views
from django.conf import settings
# from .views import User,Appliance,RegisterUser 
from .views import User,Appliance

from rest_framework import routers
from .views import UserViewSet, ApplianceViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'appliances', ApplianceViewSet)

urlpatterns = [

    path('', include(router.urls)),

    path('user', views.getUser),
    path('user/<int:id>',views.getUser),

    path('appliance', views.getAppliance),
    path('appliance/<int:id>',views.getAppliance),

] 
