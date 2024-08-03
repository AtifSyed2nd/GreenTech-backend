from django.shortcuts import render,get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from django.conf import settings

# Create your views here.

class GetUserListView(APIView):
    def get(self,request):
        users= CustomUser.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

class GetUserView(APIView):
    def get(self, request, pk):
        user =CustomUser.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        data = request.data.copy()

        # Check if password is being updated
        password = data.get('password', None)
        if password:
            user.set_password(password)
            data.pop('password')

        serializer = UserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"user_info":serializer.data,"message":"Updated Sucessfully"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(CustomUser, pk=pk)
        user.delete()
        return Response("User Deleted",status=status.HTTP_204_NO_CONTENT)

class RegisterView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        uuid_str = str(user.user_id)


        payload = {
            'id': uuid_str,
            # 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        # token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')
        # token = jwt.encode(payload,settings.SECRET_KEY, algorithm='HS256')
        token=jwt.encode(payload,settings.SECRET_KEY,algorithm='HS256')
        

        serializer = UserSerializer(user)

        return Response({"user_info": serializer.data,"token" : token})
