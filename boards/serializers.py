from rest_framework import serializers
from .models        import Board, Comment


class BoardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

class BoardDetailSerializers(serializers.ModelSerializer):
    comments = CommentSerializers(many = True)
    class Meta:
        model = Board
        fields = ['title','content','comments']