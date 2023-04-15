from django.shortcuts import redirect


def home(request):
    return redirect('/board/list/')
    # return render(request, 'home.html')

