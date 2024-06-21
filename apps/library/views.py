

from apps.library.models import Library
from apps.library.serializer import LibrarySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view,authentication_classes,permission_classes

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_library(request):
    if request.method == 'POST':
        #data = JSONParser().parse(request)
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_library(request, pk):
    if request.method == 'GET':
        try:
            lib =Library.objects.get(pk=pk)
        except Library.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        serializer = LibrarySerializer(lib)
        return Response(serializer.data)

@api_view(['GET'])
def libraries(request):
    if request.method == 'GET':
        try:
            libs= Library.objects.all()
        except Library.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = LibrarySerializer(libs,many=True)
        return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def update_library(request,pk):
    if request.method == 'PUT':
        try:
            lib = Library.objects.get(pk=pk)
        except Library.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        # data = JSONParser().parse(request)
        serializer = LibrarySerializer(lib, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_library(request, pk):
    if request.method == 'DELETE':
        try:
            lib = Library.objects.get(pk=pk)
        except Library.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        lib.delete()
        return Response(status=status.HTTP_200_OK)