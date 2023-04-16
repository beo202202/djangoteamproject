from django.db import models
# from django.contrib.auth import get_user_model
# from django_cleanup import cleanup
from user.models import UserModel
from boards.forms import Board

class Comment(models.Model):
    class Meta :
        db_table = 'comment'

    username = models.ForeignKey(UserModel(), on_delete=models.CASCADE, to_field='username')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return '{}: {}'.format(self.user.username, self.comment)

