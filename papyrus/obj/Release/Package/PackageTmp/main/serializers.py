from rest_framework import serializers
from main.models import Test, Time
#from main.models import tong6
class tong6Serializer(serializers.ModelSerializer):
    class Meta:
        #model=tong6
        fields = ('reg_num', 'date', 'datetime', 'look_code','look_codeNM', 'source', 'numeric')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields='__all__'