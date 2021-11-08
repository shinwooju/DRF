from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Board, Comment
from .serializers import BoardSerializers, BoardDetailSerializers, CommentSerializers


@api_view(['POST','GET'])
def board_list(request):
    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardSerializers(boards, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BoardSerializers(data = request.data)
        if serializer.is_valid(): #true, false
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def board_detail(request, pk):
    if request.method == 'GET':
        board = Board.objects.get(pk = pk)
        if board == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = BoardDetailSerializers(board)
        print(serializer.data)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        board = Board.objects.get(pk = pk)
        if board == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = BoardSerializers(board, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        board = Board.objects.get(pk = pk)
        if board == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        board.delete()
        return Response(status = status.HTTP_200_OK)

@api_view(['POST'])
def comments(request, pk):
    if request.method == 'POST':
        board = Board.objects.get(pk = pk)
        if board == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        request.data['board'] = board.id
        serializer = CommentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(status = status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
def comments_update(request, pk, comment_pk):
    if request.method == 'DELETE':
        comment = Comment.objects.get(pk = comment_pk)
        if comment == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        comment.delete()
        return Response(status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        comment = Comment.objects.get(pk = comment_pk)
        if comment == None:
            return Response(status = status.HTTP_404_NOT_FOUND)
        serializer = CommentSerializers(comment, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)