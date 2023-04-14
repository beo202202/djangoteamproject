from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import re


def home(request):
    user = request.user.is_authenticated  # 로그인 되어 있는지 확인
    if user:
        return render(request, 'home.html')
    else:
        return render(request, 'signin.html')


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 로그인이 되어있는지 확인
        if user:
            return redirect('/user/')
        else:
            return render(request, 'signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        email = request.POST.get('email', '')
        bio = request.POST.get('bio', '')
        
        email_check = re.compile('^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if not email_check.match(email) :
            return render(request, 'signup.html', {'error': 'email을 형식에 맞춰 작성해 주세요.'})

        if username == None or password == None:
            return render(request, 'signup.html', {'error': '올바른 값을 입력해주세요.'})

        if password != password2:
            return render(request, 'signup.html', {'error': '올바른 비밀번호를 설정해주세요.'})
        else:
            if get_user_model().objects.filter(username=username).exists():
                return render(request, 'signup.html', {'error': '중복된 아이디가 존재합니다.'})

            else:
                user = get_user_model().objects.create(username=username, email=email, bio=bio)
                user.set_password(password)
                user.save()
                return redirect('/user/sign-in')


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/user/')
        else:
            return render(request, 'signin.html', {'error': '유저이름 혹은 패스워드를 확인 해 주세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated  # 로그인 되어 있는지 확인
        if user:
            return redirect('/user/')
        else:
            return render(request, 'signin.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/user/')
