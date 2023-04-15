from django.shortcuts import render, redirect
from user.models import UserModel
from boards.models import Board
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def my_page(request, id):
    me = request.user
    click_user = UserModel.objects.get(id=id)
    board_list = Board.objects.all().filter(author_id=id)
    if me.id == id:
        show_my_board = True
    else:
        show_my_board = False
    return render(request, 'mypage/my_page.html', {'click_user': click_user, 'board_list': board_list, 'show_my_board': show_my_board})


# 팔로워 활용 가능
# @login_required
# def view_users(request):
#     if request.method == 'GET':
#         me = request.user
#         all_user = UserModel.objects.all().exclude(id=me.id)
#     return render(request, 'home.html', {'all_user': all_user})


@login_required
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()

        context = {
            'form': form,
        }
        return render(request, 'mypage/profile_modify.html', context)
    else:
        form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'mypage/profile_modify.html', context)

