from django.contrib import admin

from .models import Board,Comment

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
