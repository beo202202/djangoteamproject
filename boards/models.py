from django.db import models
from django.contrib.auth import get_user_model


class Board(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True, default=None)

    class Meta:
        db_table = 'board'
