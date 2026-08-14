from django.contrib.auth.models import User 
from django.contrib.auth import authenticate

from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from rest_framework.authtoken.models import Token 

from .serializers import * 

# I asked AI to help with CBV for User
class RegisterAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        
        user = User.objects.create_user(
            username = serializer.validated_data['username'],
            password = serializer.validated_data['password']
        )
        
        return Response(
            {
                'id': user.id,
                'username': user.username
            },
            status=status.HTTP_201_CREATED
        )

class AuthorizationAPIView(APIView):

    def post(self, request):
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if not user:
            return Response(
                {'detail': 'Invalid username or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key
        })

