from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)
# Create your views here.
class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입 성공"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response("get")
    
class Update(APIView):
    def post(self, request,email,date_of_birth):
        serializer = UserSerializer.update(email, date_of_birth)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"변경 성공"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

