from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from data.models import Report
from api.serializers import ReportSerializer

from data.permissions import ReportPermissions


@api_view(['POST', 'GET', 'DELETE'])
@permission_classes([ReportPermissions])
def report_views(request, id=None):
    response = {}
    if request.method == 'GET':
        user = ReportSerializer(Report.objects.all(), many=True, context={'request': request}).data

        response['reports'] = user

        return Response(response, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        try:
            if not id:
                response['message'] = f"Tidak ada id user yang diberikan"
                return Response(response, status=status.HTTP_404_NOT_FOUND)
            report = Report.objects.get(id=id)
            report.delete()

            response['message'] = f'Berhasil menghapus report dengan id {id}'

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            response['message'] = str(e)
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    elif request.method == "POST":
        try:
            report = ReportSerializer(data=request.data)
            if report.is_valid():
                report.save()
                response['message'] = 'Report baru sudah berhasil terbuat'
                return Response(response, status=status.HTTP_201_CREATED)

            response['errors'] = report.errors
            return Response(response, status=status.HTTP_500_OK)
        except Exception as e:
            response['error'] = str(e)
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)