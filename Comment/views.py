from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

# Create your views here.
def comment(request, board_id):
    comment = Comment.object.get(board_id=board_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.board_id = board_id
            comment.save()
            return redirect('/board/detail/', board_id=board_id)
    else:
        form = CommentForm
        
    return render(request, 'comment.html', {'form'}:form)