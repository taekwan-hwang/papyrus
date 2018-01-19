from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from main.serializers import TestSerializer, TimeSerializer, Tong2Serializer, Tong5Serializer, Tong8Serializer
from main.cycle_divider import get_by_cycle, get_by_person, mean_pain_variance_by_cycle
from main.models import Tong2, Tong5, Tong8
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
        serializer=TimeSerializer(get_by_person(3), many=True)
        return Response(serializer.data)

class TestVarianceMean(APIView):
    def get(self, request, format=None):
        return Response(mean_pain_variance_by_cycle(1))

class Tong2View(APIView):
    def get(self, request, format=None, pi=0):
        objects=Tong2.objects.filter(pi=pi).filter(n_attr_codeNM='통증 강도').order_by('actual_datetime')
        list=[]
        for obj in objects:
            list.append({'pain':obj.attr,'daytime':obj.actual_datetime})
        return Response(list)

class Tong5View(APIView):
    def get(self, request, format=None, pi=0):
        serializer=Tong5Serializer(Tong5.objects.filter(pi=pi).order_by('format_date').last())
        return Response(serializer.data)

class Tong8View(APIView):
    def get(self, request, format=None, pi=0):
        serializer=Tong8Serializer(Tong8.objects.filter(pi=pi).filter(prescription_code='L100907200').order_by('sampling_time').last())
        return Response(serializer.data)