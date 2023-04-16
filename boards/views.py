from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, CreateView, DeleteView
from .models import Board
# from django.urls import reverse_lazy, reverse
from .forms import BoardForm
# from django.http import HttpResponse
import os
from PIL import Image
from comments.models import Comment
from bookmarks.models import Bookmark


# Create your views here.
# 추후 로그인 리콰이어

# APIView는 RESTful API를 만들기 위해 Djnago에서 제공하는 클래스 기반 뷰 중 하나
# RESTful API를 작성하는 데 필요한 다양한 기능을 제공한다.
# 요청과 응답을 직렬화하는 Serializer, 이증과 권한을 다루는 Permission 및 Authentication 클래스 등을 제공
# 각 HTTP 메서드(get,post,put,delete 등)에 대한 기본적인 구현을 제공
# 이를 오버라이드하여 원하는 기능을 구현 가능
# 그래서 APIView를 사용

class Boards(View):

    def get(self, request):
        form = BoardForm()
        return render(request, 'board/board_create.html', {'form': form})

    def post(self, request):
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            board = form.save(commit=False)
            board.author = request.user
            # board.img = request.FILES.get('img')    # 이미지 주소 받아오기

            # 이미지 파일 압축하기
            if board.img:
                image_path = board.img.path
                if os.path.exists(image_path):
                    compressed_image_path = image_path.replace(
                        ".jpg", "_compressed.jpg")
                    image = Image.open(image_path)
                    image = image.convert('RGB')
                    image.save(compressed_image_path,
                               optimize=True, quality=70)
                    board.img.name = compressed_image_path.split("/")[-1]

            board.save()

            return redirect('/board/list/')  # 상세보기로 가기
            # return render(request, '/board_create.html')
        # except Exception as e:
        #     return render(request, 'error.html', {'error_message': str(e)})

        # return render(request, 'error.html')

    def delete(self, request, board_id):
        Board.objects.get(board_id=board_id).delete()
        return redirect('/board/list/')
        # 이미지는 media에서도 삭제됨 휴..


class BoardList(View):
    def get(self, request):
        if request.method == 'GET':
            boards = Board.objects.all().order_by('-updated_at')

            return render(request, 'board/board_list.html', {'boards': boards})
        return redirect('/board/')


# django에서 제공하는 detailview를 활용함
# class BoardDetail(DetailView):
#     model = Board
#     template_name = 'board/board_detail.html'

def board_detail(request, board_id):
    board = Board.objects.get(board_id=board_id)
    comments = Comment.objects.filter(board=board)

    is_bookmarked = False
    if request.user.is_authenticated:
        user_bookmarks = Bookmark.objects.filter(user=request.user)
        if user_bookmarks.filter(boards=board).exists():
            is_bookmarked = True

    # bookmarks = Bookmark.objects.filter(board_id=board_id).count
    # , 'bookmarks': bookmarks}
    context = {'board': board, 'comments': comments,
               'is_bookmarked': is_bookmarked}
    return render(request, 'board/board_detail.html', context)


# @login_required()
def board_edit(request, board_id):
    board = Board.objects.get(board_id=board_id)
    if request.method == "POST":
        board.content = request.POST['content']
        if 'img' in request.FILES:  # 새로운 이미지가 업로드된 경우
            board.img.delete()          # 기존 이미지 삭제
            board.img = request.FILES.get('img')    # 새로운 이미지 저장

            # 이미지 파일 압축하기
            image_path = board.img.path
            compressed_image_path = image_path.replace(
                ".jpg", "_compressed.jpg")
            image = Image.open(image_path)
            image = image.convert('RGB')
            image.save(compressed_image_path, optimize=True, quality=70)
            board.img.name = compressed_image_path.split("/")[-1]

            board.save()

        board.save()

        return redirect('board_detail', board_id=board.board_id)

    else:
        return render(request, 'board/board_edit.html', {'board': board})


@login_required
def likes(request, board_id):
    board = Board.objects.get(board_id=board_id)

    if request.method == 'GET':
        if board.likes.filter(id=request.user.id).exists():
            board.likes.remove(request.user)
            board.update_likes_count()
        else:
            board.likes.add(request.user)
            board.update_likes_count()

        return redirect('board_detail', board_id=board_id)
    context = {'board': board, 'likes_count': board.likes_count}
    return render(request, 'board/board_detail.html', context)
