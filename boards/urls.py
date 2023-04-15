from django.urls import path
from . import views
from boards import views
from boards.views import Boards, BoardList

urlpatterns = [
    path('list/', BoardList.as_view(), name='board-list'),
    path('', Boards.as_view(), name='board-create'),
    path('<int:board_id>/', Boards.as_view(), name='board-delete'),
    path('detail/<int:board_id>/', views.board_detail, name='board_detail'),
    path('edit/<int:board_id>/', views.board_edit, name='board_edit'),
    path('<int:board_id>/likes/', views.likes, name='likes'),    
]
