
from apps.book.models import Book
from apps.book.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['POST'])
def create_book(request):
    if request.method == 'POST':
        serializer =BookSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_book(request, pk):
    if request.method == 'GET':
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        serializer = Book(book)
        return Response(serializer.data)

@api_view(['GET'])
def books(request):
    if request.method == 'GET':
        try:
            books= Book.objects.all()
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def update_book(request,pk):
    if request.method == 'PUT':
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        # data = JSONParser().parse(request)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_book(request, pk):
    if request.method == 'DELETE':
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        book.delete()
        return Response(status=status.HTTP_200_OK)