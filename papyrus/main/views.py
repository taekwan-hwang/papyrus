from django.shortcuts import render

# Create your views here.
from main.models import tong6
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.serializers import tong6Serializer

class Tong6List(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        query_set=tong6.objects.all()
        serializer = tong6Serializer(query_set, many=True)
        return Response(serializer.data)