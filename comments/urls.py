from django.urls import path
from . import views

urlpatterns = [
    # ... 다른 URL 패턴들 ...
    path('<int:board_id>/', views.comment, name='comment'),
    path('<int:board_id>/<int:comment_id>/', views.comment_edit, name='comment-edit'),
    path('<int:board_id>/<int:comment_id>/delete', views.comment_delete, name='comment-delete'),    
]