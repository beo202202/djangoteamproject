from django.urls import path
from . import views

urlpatterns = [
    # ... 다른 URL 패턴들 ...
    path('<int:board_id>/', views.comment, name='comment'),
]