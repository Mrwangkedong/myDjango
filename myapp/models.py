from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')
    content = models.TextField(null=True)
    # put_time = models.DateTimeField(auto_now=True)
    put_time = models.DateTimeField(null=True)  # 设为null = True 就可以在admin中进行修改

    def __str__(self):
        return self.title