from django.db import models
# from django.contrib.auth import get_user_model
# from django_cleanup import cleanup
from user.models import UserModel
from boards.forms import Board

class Comment(models.Model):
    author = models.ForeignKey(UserModel(), on_delete=models.CASCADE)
    board_id = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comment_board')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        db_table = 'comment'