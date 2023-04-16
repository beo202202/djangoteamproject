from django.db import models
from user.models import UserModel


class Bookmark(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    boards = models.ManyToManyField('boards.board', related_name='bookmarks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + ": " + self.articles.content

    class Meta:
        db_table = 'bookmark'
