from django.db import models
# from django.contrib.auth import get_user_model
# from django_cleanup import cleanup
from user.models import UserModel


class Board(models.Model):
    author = models.ForeignKey(UserModel(), on_delete=models.CASCADE)
    board_id = models.AutoField(primary_key=True)
    # title = models.CharField(max_length=50)
    img = models.FileField(null=True, upload_to="", blank=True)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(UserModel, related_name='likes', blank=True)
    likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'board'
        
    #좋아요 저장
    def update_likes_count(self):
        self.likes_count = self.likes.count()
        self.save()

    # def delete(self, *args, **kargs):
    #     os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_file.name))
    #     super(Board, self).delete(*args, **kargs)