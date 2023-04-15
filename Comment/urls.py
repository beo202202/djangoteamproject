from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('<int:board_id>/comment/', views.comment, name='comment',)
]