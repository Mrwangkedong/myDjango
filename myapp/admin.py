from django.contrib import admin
from . import models

# Register your models here.
#显示其他字段
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','put_time')
    list_filter = ('put_time',)


admin.site.register(models.Article,ArticleAdmin)