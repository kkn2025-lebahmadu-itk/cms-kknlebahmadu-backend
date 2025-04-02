from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from data.models import Complaint
from data.permissions import ComplaintPermission
from api.serializers import ComplaintSerializer

from django.shortcuts import get_object_or_404

# @api_view(['POST'])
# @permission_classes([AdminOnly])
# def create_complaint(request):
#     return "Complaint created"


# @api_view(['GET'])
# @permission_classes([AdminOnly])
# def create_complaint(request):
#     return "Complaint fetched"


# @api_view(['PUT'])
# @permission_classes([AdminOnly])
# def create_complaint(request):
#     return "Complaint updated"


@api_view(['GET', 'POST', 'PUT'])
@permission_classes([ComplaintPermission])
def complain_views(request, id=None):
    response = {}

    if request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response['message'] = 'Keluhan berhasil dibuat'
            return Response(response, status=status.HTTP_201_CREATED)
        
        response['message'] = 'Terjadi Kesalahan'
        response['error'] = serializer.errors
        return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'GET':
        serializer = ComplaintSerializer(Complaint.objects.all(), many=True)

        response['message'] = 'Berhasil emngambil keluhan'
        response['data'] = serializer.data

        return Response(response, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        complaint = get_object_or_404(Complaint, id=id)
        new_status = request.data.get('status')

        # Data status yang valid :
        # "selesai"
        # "progress"
        # "tidak_valid"
        # "sudah_dibaca"
        # "pending"

        if not new_status:
            response['message'] = 'Status baru tidak ditemukan'
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        complaint.status = new_status
        complaint.save()

        response['message'] = 'Status berhasil diubah'

        return Response(response, status=status.HTTP_200_OK)