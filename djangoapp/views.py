from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Rishab
from .serializer import RishabSerializer

@api_view(['GET','POST'])
def RishabViewList(resquest):
    if resquest.method =='GET':
        rishab=Rishab.objects.all()
        rishabSerializer=RishabSerializer(rishab,many=True)
        return Response(rishabSerializer.data)
    
    elif resquest.method == 'POST':
        rishabSerializer=RishabSerializer(data=resquest.data)
        if rishabSerializer.is_valid():
            rishabSerializer.save()
            return Response(rishabSerializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(rishabSerializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def RishabDetailsList(request,pk):
    try:
        rishab=Rishab.objects.get(pk=pk)    
    except Rishab.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    if request.method=='GET':
        rishabSerializer=RishabSerializer(rishab)
        return Response(rishabSerializer.data)
    
    elif request.method =='PUT':
        rishabSerializer=RishabSerializer(rishab , data=request.data)
        if rishabSerializer.is_valid():
            rishabSerializer.save()
            return Response(rishabSerializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(rishabSerializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        rishab.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        