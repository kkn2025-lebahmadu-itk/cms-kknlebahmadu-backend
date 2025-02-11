from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from data.models import User

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    response = {}
    
    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        response['message'] = "pengguna berhasil terdaftar"
        return Response(response)
    except Exception as e:
        print(e)
        response['message'] = "Terjadi kesalahan"
        response['data'] = str(e)
        return Response(response)