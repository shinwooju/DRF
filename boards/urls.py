from django.urls import path

from .views import board_list, board_detail, comments, comments_update


app_name = 'boards'
urlpatterns = [
    path('', board_list),
    path('<int:pk>/', board_detail),
    path('<int:pk>/comments/', comments),
    path('<int:pk>/comments/<int:comment_pk>', comments_update)
]