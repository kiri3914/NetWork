from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    title = models.CharField(max_length=255, verbose_name='Название Поста')
    data_created = models.DateField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    unlikes = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return f'Пользователь {self.owner.username} добавил пост {self.title}'


class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Пользователь {self.owner.username} Лайкнул пост {self.post.title}'


class UnLike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='unlike')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    data_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Пользователь {self.owner.username} Диздайкнул пост {self.post.title}'
