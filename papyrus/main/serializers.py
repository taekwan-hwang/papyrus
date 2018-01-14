from rest_framework import serializers
from main.models import Test
#from main.models import tong6
class tong6Serializer(serializers.ModelSerializer):
    class Meta:
        #model=tong6
        fields = ('reg_num', 'date', 'datetime', 'look_code','look_codeNM', 'source', 'numeric')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'