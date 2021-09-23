from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    meta_description = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name





class Content(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_Post')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name='products')
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True, null=True)
    viewcount = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        index_together = [['id','slug']]

    def __str__(self):
        return "카테고리 : " + self.category.name + " / 작성자 : " + self.author.username + "/     제목 :  " + self.title + "/ 작성일자 :" + self.created.strftime("-%Y-%m-%d %H:%M")


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Content, on_delete=models.CASCADE)

    def __str__(self):
        return "작성자 : " + self.author + "댓글 : " + self.comment


class Like(models.Model):
    Content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="likes")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")

    created = models.DateTimeField(auto_now_add=True)




