from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.serializers import TestSerializer, TimeSerializer
from main.cycle_divider import get_by_cycle, get_by_person
class TestGetByCycle(APIView):
    def get(self, request, format=None):
        serializer=TestSerializer(get_by_cycle(1), many=True)
        return Response(serializer.data)
    """
    List all snippets, or create a new snippet.
    """
    """
    def get(self, request, format=None):
        query_set=tong6.objects.all()
        serializer = tong6Serializer(query_set, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        name=str(request.data.get('name', 'taekwan'))
        num=str(request.data.get('num', '123'))
        query_set=tong6.objects.filter(reg_num=499324)
        serializer = tong6Serializer(query_set, many=True)
        return Response(name+num)
    """
class TestGetByPerson(APIView):
    def get(self, request, format=None):
        serializer=TimeSerializer(get_by_person(), many=True)
        return Response(serializer.data)