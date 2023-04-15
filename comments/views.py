from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

# Create your views here.
def comment(request, board_id):    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.username = request.user
            comment.board_id = board_id
            comment.save()
            return redirect('/board/detail/{}/'.format(board_id))
    else:        
        comment = Comment.objects.get(board_id=board_id)
        form = CommentForm()
        context = {'form': form }
        
    return render(request, 'board/board_detail.html', context)


