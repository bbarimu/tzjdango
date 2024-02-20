from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length = 100
    )
    def __str__(self):
        return f'{self.name}'
class Author(models.Model):
    full_name = models.CharField(
        max_length = 125
    )
    def __str__(self):
        return f"{self.full_name} | {self.pk}"


class Post(models.Model):
    title = models.CharField(
        max_length = 100,
        verbose_name = 'имя'
    )
    content = models.TextField(
        max_length = 1000,
        verbose_name = 'текст'
    )
    category = models.ForeignKey(
        Category,on_delete = models.PROTECT
    )
    author = models.ForeignKey(
        Author,on_delete = models.PROTECT
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__(self):
        return f"{self.title} | {self.pk}"