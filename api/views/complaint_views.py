from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from data.models import User, News
from data.permissions import AdminOnly
from api.serializers import ComplaintSerializer

from django.shortcuts import get_object_or_404