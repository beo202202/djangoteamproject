from django.db import models


class Board(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'board'
