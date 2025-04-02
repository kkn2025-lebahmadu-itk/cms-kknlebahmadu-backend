from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from data.models import Profile
from data.permissions import ProfilePermissions
from api.serializers import ProfileSerializer

from django.shortcuts import get_object_or_404

@api_view(['POST', 'GET', 'DELETE', 'PUT'])
@permission_classes([ProfilePermissions])
def profile_views(request, id=None):
    response = {}

    # Valid type = 'inti' dan 'tambahan'

    if request.method == 'GET':
        inti = ProfileSerializer(Profile.objects.filter(type='inti'), many=True).data
        tambahan = ProfileSerializer(Profile.objects.filter(type='tambahan'), many=True).data

        response['message'] = 'Berhasil mengambil data profile dari server'
        response['data'] = {
            'inti': inti,
            'tambahan': tambahan
        }
        return Response(response, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['message'] = 'Profile baru berhasil ditambah'
            return Response(response, status=status.HTTP_201_CREATED)

        response['message'] = 'Terjadi kesalahan'
        response['error'] = serializer.errors
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'DELETE':
        profile = get_object_or_404(Profile, id=id)
        profile.delete()
        response['message'] = 'Data berhasil dihapus'
        return Response(response)

    elif request.method == 'PUT':
        profile = get_object_or_404(Profile, id=id)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['message'] = f'Data berhasil diubah'
            return Response(response, status=status.HTTP_200_OK)

        response['message'] = 'Terjadi kesalahan'
        response['error'] = serializer.errors
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)