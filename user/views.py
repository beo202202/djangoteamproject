from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.http import HttpResponse
import re

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.encoding import force_bytes, force_str


def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated  # 로그인이 되어있는지 확인
        if user:
            return redirect('/board/list')
        else:
            return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)
        email = request.POST.get('email', '')
        bio = request.POST.get('bio', '')

        email_check = re.compile(
            '^[a-zA-Z0-9+-\_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        if not email_check.match(email):

            return render(request, 'user/signup.html', {'error': 'email을 형식에 맞춰 작성해 주세요.'})

        if username == None or password == None:
            return render(request, 'user/signup.html', {'error': '올바른 값을 입력해주세요.'})

        if password != password2:
            return render(request, 'user/signup.html', {'error': '올바른 비밀번호를 설정해주세요.'})
        else:
            if get_user_model().objects.filter(username=username).exists():
                return render(request, 'user/signup.html', {'error': '중복된 아이디가 존재합니다.'})

            else:
                user = get_user_model().objects.create(username=username, email=email, bio=bio)
                user.set_password(password)
                user.is_active = False
                user.save()

                current_site = get_current_site(request)

                message = render_to_string('user/activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                mail_title = "계정 활성화 확인 이메일"
                mail_to = request.POST["email"]
                email = EmailMessage(mail_title, message, to=[mail_to])
                email.send()
                return HttpResponse(
                    '<div style="font-size: 40px; width: 100%; height:100%; display:flex; text-align:center; '
                    'justify-content: center; align-items: center;">'
                    '입력하신 이메일<span>로 인증 링크가 전송되었습니다.</span>'
                    '</div>'
                )


def sign_in_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        me = auth.authenticate(request, username=username, password=password)

        if me is not None:
            auth.login(request, me)
            return redirect('/board/list')
        else:
            return render(request, 'user/signin.html', {'error': '유저이름 혹은 패스워드를 확인 해 주세요'})

    elif request.method == 'GET':
        user = request.user.is_authenticated  # 로그인 되어 있는지 확인
        if user:
            return redirect('/board/list')
        else:
            return render(request, 'user/signin.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect('/board/list')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExsit):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        auth.login(request, user)
        return redirect("/board/list/")
    else:
        return HttpResponse('계정활성화 오류, 이메일을 확인해주세요')

