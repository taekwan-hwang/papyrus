from rest_framework import serializers
from main.models import Test, Time, Tong2, Tong5, Tong8
#from main.models import tong6
"""class tong6Serializer(serializers.ModelSerializer):
    class Meta:
        #model=tong6
        fields = ('reg_num', 'date', 'datetime', 'look_code','look_codeNM', 'source', 'numeric')
"""

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields='__all__'

class Tong2Serializer(serializers.ModelSerializer):
    class Meta:
        model=Tong2
        fields='__all__'

class Tong5Serializer(serializers.ModelSerializer):
    class Meta:
        model=Tong5
        fields='__all__'

class Tong8Serializer(serializers.ModelSerializer):
    class Meta:
        model=Tong8
        fields='__all__'