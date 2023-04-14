from django.db import models
# from django_cleanup import cleanup


class Board(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    img = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'board'

    # def delete(self, *args, **kargs):
    #     os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_file.name))
    #     super(Board, self).delete(*args, **kargs)
