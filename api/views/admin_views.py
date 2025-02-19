from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from data.models import User
from api.serializers import UserSerializer

from data.permissions import SuperuserOnly


@api_view(['POST', 'GET', 'DELETE'])
@permission_classes([SuperuserOnly])
def admin_views(request, id=None):
    response = {}
    if request.method == 'GET':
        user = UserSerializer(User.objects.all(), many=True).data
        admin = UserSerializer(User.objects.filter(role="admin"), many=True).data

        response['users'] = user
        response['admins'] = admin

        return Response(response, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        try:
            print(id)
            if not id:
                response['message'] = f"Tidak ada id user yang diberikan"
                return Response(response, status=status.HTTP_404_NOT_FOUND)
            user = User.objects.get(id=id)

            if user.role == 'superuser':   
                response['message'] = "Tidak bisa menghilangkan status admin superuser"
                return Response(response, status=status.HTTP_403_FORBIDDEN)

            user.role = 'user'
            user.save()

            response['message'] = f'Berhasil menghilangkan status admin user dengan id {id}'

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response['message'] = str(e)
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == "POST":
        print(request.user)
        try:
            if not id:
                response['message'] = "Tidak id user yang dibreikan"
                return Response(response, status=status.HTTP_404_NOT_FOUND)
            user = User.objects.get(id=id)

            user.role = "admin"
            user.save()

            response['message'] = f"User dengan id {id} berhasil dibuat menjadi admin"
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response['error'] = str(e)
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)