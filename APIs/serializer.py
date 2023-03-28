from rest_framework import serializers 
from .models import User,Appliance
# from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','u_name','u_location','u_login','u_rights','email','mobile','status','is_active']

class ApplianceSerializer(serializers.ModelSerializer):
    # Forkey = UserSerializer() #This line shows complete data of user in Appliances Table
    class Meta:
        model = Appliance
        fields=['id','A_name','A_category','A_watt','A_consumption','Forkey']