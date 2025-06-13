from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from data.models import User
from django.contrib.auth import authenticate

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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    response = {}

    email = request.user.email
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')

    if not old_password or not new_password:
        response['message'] = "Password lama dan baru harus diisi"
        return Response(response, status=400)

    user = authenticate(email=email, password=old_password)

    if user is None:
        response['message'] = "Password lama salah"
        return Response(response, status=400)

    try:
        user.set_password(new_password)
        user.save()

        response['message'] = "Password berhasil diubah"
        return Response(response)
    except Exception as e:
        print(e)
        response['message'] = "Terjadi kesalahan"
        response['data'] = str(e)
        return Response(response, status=500)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_user(request):
    response = {}
    
    try:
        user = request.user
        response['message'] = "Berhasil mendapatkan data pengguna"
        response['user'] = {
            'id': user.id,
            'name': user.username,
            'role': user.role
        }
        return Response(response)
    except Exception as e:
        print(e)
        response['message'] = "Terjadi kesalahan"
        response['data'] = str(e)
        return Response(response)