from django.db import models


class Category(models.Model):
    class Meta:
        db_table = "category"  # 원하는 db 이름

    def __str__(self):
        return self.category

    category = models.CharField(max_length=100)


class Article(models.Model):
    class Meta:
        db_table = "article"  # 원하는 db 이름

    title = models.CharField(max_length=20, null=False)  # 길이 제한 옵션을 줄 수도 있다
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.CharField(max_length=256, default='')
