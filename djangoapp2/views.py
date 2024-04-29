from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Abhishek
from .serializer import AbhishekSerializers


@api_view(['GET','POST'])
def AbhishekViewList(request):
    if request.method == 'GET':
        abhishek=Abhishek.objects.all()
        abhishekSerializers=AbhishekSerializers(abhishek , many=True)
        return Response(abhishekSerializers.data)
    
    elif request.method == 'POST':
        abhishekSerializers=AbhishekSerializers(data=request.data)
        if abhishekSerializers.is_valid():
            abhishekSerializers.save()
            return Response(abhishekSerializers.data)
        else:
            return Response(abhishekSerializers.errors, status=status.HTTP_404_NOT_FOUND)
        
        
@api_view(['GET' ,'PUT', 'DELETE'])       
def AbhishekDetailsList(resquest , pk ):
    try:
        abhishek=Abhishek.objects.get(pk=pk)
    except Abhishek.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if resquest.method == 'GET':
        abhishekSerializers=AbhishekSerializers(abhishek )
        return Response(abhishekSerializers.data)
    
    elif resquest.method == 'PUT':
        abhishekSerializers=AbhishekSerializers(abhishek , data=resquest.data)
        if abhishekSerializers.is_valid():
            abhishekSerializers.save()
            return Response(abhishekSerializers.data)
        else:
            return Response(abhishekSerializers.errors, status=status.HTTP_404_NOT_FOUND)
        
    elif resquest.method =='DELETE':
        abhishek.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)