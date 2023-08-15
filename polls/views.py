from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.status import HTTP_201_CREATED
from .models import TelChopModel
from .serializer import TelChopSerializer
# Create your views here.


class get_all(APIView):
    def get(self,request,*args,**kwargs):
        all_data = TelChopModel.objects.all()
        serializer = TelChopSerializer(all_data, many=True)
        return Response(serializer.data)
    # end def
    
class index(APIView):
    def post(self,request,*args,**kwargs):
        teacher = get_object_or_404(TelChopModel, id = kwargs['id'])
        serializer = TelChopSerializer(teacher)
        return Response(serializer.data)
        
    # end def
    
class Delete(APIView):
    def delete(self, request, *args,**kwargs):
        teacher = get_object_or_404(TelChopModel, id = kwargs['id'])
        teacher.delete()
        return Response({'msg':'deleted'})
        
    # end def

class Updete(APIView):
    def patch(self, request,*args,**kwargs):
        teacher = get_object_or_404(TelChopModel, id = kwargs['id'])
        serializer = TelChopSerializer(teacher,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    # end def
    
class Create(APIView):
    def post(self, request,*args,**kwargs):
        serializer = TelChopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors)
    # end def