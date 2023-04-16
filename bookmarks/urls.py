from django.urls import path
from .views import BookmarkList, add_bookmark

app_name = 'bookmarks'

urlpatterns = [
    path('<int:board_id>/', add_bookmark, name='add_bookmark'),
    path('', BookmarkList.as_view(), name='bookmark_list'),
]
