from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    title = models.CharField(max_length=255, verbose_name='Название Поста')
    text = models.TextField(verbose_name='Текст Поста')
    data_create = models.DateField(auto_now_add=True)
    like = models.PositiveIntegerField(default=0)
    unlike = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Пользователь {self.user.username} добавил пост {self.title}'


