from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

# Create your views here.
# 댓글 기능추가
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



#댓글 수정기능
def comment_edit(request, comment_id, board_id):
    comment = Comment.objects.get(id=comment_id)
    form = CommentForm(instance=comment)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/board/detail/{}'.format(board_id))
    return render(request, 'board/board_detail.html', {'form': form}) 

#댓글 삭제기능
def comment_delete(request, comment_id, board_id):
    comment = Comment.objects.get(id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('/board/detail/{}/'.format(board_id))
    return render(request, 'board/board_detail.html')

