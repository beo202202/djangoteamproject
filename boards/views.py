from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, ListView, CreateView, DeleteView
from .models import Board
from django.urls import reverse_lazy, reverse
from .forms import BoardForm
from django.http import HttpResponse


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
            title = request.POST['title']
            content = request.POST['content']
            # post_author = 유저id
            img = request.FILES.get('img')  # 이미지 주소 받아오기
            board = Board.objects.create(
                title=title, content=content, img=img)
            board.save()

            return redirect('/board/list/')  # 상세보기로 가기
        # return render(request, '/board_create.html')

    def delete(self, request, board_id):
        Board.objects.get(board_id=board_id).delete()
        return redirect('/board/list/')


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
    return render(request, 'board/board_detail.html', {'board': board})


# @login_required()
def board_edit(request, board_id):
    board = Board.objects.get(board_id=board_id)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        # board.board_id = request.POST['id']
        board.img = request.FILES.get('img')
        if img:  # 이미지가 업로드되었을 경우
            board.img = img
        board.save()
        return redirect('board_detail', board_id=board.board_id)

    else:
        return render(request, 'board/board_edit.html', {'board': board})
