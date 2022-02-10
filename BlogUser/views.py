import imp
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from .serializers import RegistrationSerializer, ListUserSerializer

from .models import User

# Create your views here.
class RegistrationAPIView(APIView):
    def get(self, request):
        return Response('Make a post request')

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            token = Token.objects.get_or_create(user=User.objects.get(email=request.data['email']))[0].key # (key, _)
            return Response({"key": token})
        return Response(serializer.errors)


class UserLoginAPIView(APIView):
    def get(self, request):
        return Response('To Login Use Post Request', status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        if 'email' in request.data and 'password' in request.data:
            try:
                user = User.objects.get(email=request.data['email'])
                if not user.check_password(request.data['password']):
                    return Response('Incorrect Password', status=status.HTTP_400_BAD_REQUEST)
                token = Token.objects.get_or_create(user=user)[0].key # (key, _)
                return Response({"key": token})
                # Extract Key
            except User.DoesNotExist:
                return Response('Invalid Email Id', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Either Email or password is missing', status=status.HTTP_400_BAD_REQUEST)

    

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response('Successfully Logged Out', status=status.HTTP_200_OK)

class ListUserAPIView(APIView):
    permisssion_classes = (IsAuthenticated)

    def get(self, request):
        users = User.objects.all()  # Queryset
        serializer = ListUserSerializer(users, many=True)
        return Response(serializer.data)



class UserDetailAPIView(APIView):
    permisson_classes=(IsAuthenticated)

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
            if user == request.user:
                serializer = ListUserSerializer(user)
                return Response(serializer.data)
            return Response('Different User')
        except User.DoesNotExist:
            return Response('Invalid Id', status=status.HTTP_400_BAD_REQUEST)



