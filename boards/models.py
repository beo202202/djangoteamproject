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

    class Meta:
        db_table = 'board'

    # def delete(self, *args, **kargs):
    #     os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_file.name))
    #     super(Board, self).delete(*args, **kargs)
