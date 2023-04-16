from django.shortcuts import render, redirect
from django.views.generic import View
# from .forms import BookmarkForm
from .models import Bookmark
from django.contrib.auth.decorators import login_required
from boards.models import Board
from django.contrib import messages


@login_required
def add_bookmark(request, board_id):
    board = Board.objects.get(pk=board_id)
    user_bookmarks = Bookmark.objects.filter(user=request.user)
    if user_bookmarks.filter(boards=board).exists():
        # 북마크에 있는 게시글
        messages.warning(request, '이미 북마크에 추가된 게시글입니다.')
    else:
        # 북마크에 없는 게시글
        bookmark = Bookmark.objects.create(user=request.user)
        bookmark.boards.add(board)
        messages.success(request, '게시글이 북마크에 추가되었습니다.')

    return redirect('board_detail', board_id=board_id)


@login_required
class Bookmarklist(View):
    def get(self, request):
        # form = BookmarkForm()

        bookmarks = Bookmark.objects.filter(user=request.user)
        context = {'bookmarks': bookmarks}
        return render(request, 'bookmark/bookmark_list.html', context)


# def bookmark_list(request):

#     bookmarks = request.user.bookmark_set.all()
#     context = {'bookmarks': bookmarks}
#     return render(request, 'bookmark/bookmark_list.html', context)
