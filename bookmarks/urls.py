from django.urls import path
from bookmarks.views import Bookmarklist, add_bookmark
from django.contrib import messages

app_name = 'bookmarks'


urlpatterns = [
    path('<int:board_id>/', add_bookmark, name='add_bookmark'),
    # path('', Bookmarklist.as_view(), name='bookmark_list'),
    # path('add/<int:pk>', Bookmarks.as_view(), name='add_bookmark'),
    # path('', bookmark_list, name='bookmark_list'),
]
