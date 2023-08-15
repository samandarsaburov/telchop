from rest_framework import serializers
from .models import TelChopModel

class TelChopSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = TelChopModel
        fields = ('id','model','tel_haqida','creat_date','update_date','del_date','status')