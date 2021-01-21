from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
import myapp.views as mv

urlpatterns = [
    path('index/',mv.index),
    path('article/<int:article_id>/',mv.article_page,name= 'article_page'),
    path('edit/<int:article_id>/',mv.article_edit,name='article_edit'),
    path('edit/action/',mv.edit_action,name='edit_action'),
    path('upload_file/',mv.upload_file,name='upload_file'),
    path('upload_index/',mv.upload_html),
    path('chaifen/',mv.TVCS_chai),
    path('hebing/',mv.TVCS_he),
]
#django2.0之后
app_name = 'myapp'
