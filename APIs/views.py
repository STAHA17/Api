from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView  
from .models import User,Appliance
from .serializer import UserSerializer,ApplianceSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly



# class RegisterUser(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if not serializer.is_valid():
#             return response(serializer.errors)
#         serializer.save()
#         user=User.objects.get(u_name=serializer.data['u_name'])
#         token_obj , _ = Token.objects.get_or_create(user=user)
#         return response({'status':200, 'payload':serializer.data , 'token':str(token_obj)})

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    # authentication_classes=[TokenAuthentication]
    # permissions_classes=[IsAuthenticated]
    queryset = User.object.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def getUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response({'user':serializer.data},status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def postUser(request):

    data = {
            'id': request.user.id ,
            'u_name': request.data.get('u_name'), 
            'u_location': request.data.get('u_location'), 
            'u_login': request.data.get('u_login'), 
            'u_rights': request.data.get('u_rights'),
            'email': request.data.get('email'),
            'mobile': request.data.get('mobile'),
            'status': request.data.get('status'),
            'is_staff': request.data.get('is_staff'),
            # 'is_active': request.data.get('is_active'),

    }

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'user':serializer.data},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @api_view(['GET','PUT','DELETE']) 

    def update(self, request, *args, **kwargs):
        #partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def getAppliance(request):
    appliance = Appliance.objects.all()
    serializer = ApplianceSerializer(appliance, many=True)
    return Response({'appliance':serializer.data},status=status.HTTP_200_OK)

@api_view(['POST'])
def postAppliance(request):
    data = {
            'id': request.user.id ,
            'A_name': request.data.get('A_name'), 
            'A_category': request.data.get('A_category'), 
            'A_watt': request.data.get('A_watt'), 
            'A_consumption': request.data.get('A_consumption'),
    }

    serializer = ApplianceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'appliance':serializer.data},status=status.HTTP_200_OK) 

class ApplianceViewSet(viewsets.ModelViewSet):
    queryset = Appliance.objects.all()
    serializer_class = ApplianceSerializer

    # @api_view(['GET','PUT','DELETE']) 

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)