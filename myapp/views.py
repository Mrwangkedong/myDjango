from django.shortcuts import render  #渲染
from myapp.models import Article
from django.http import HttpResponse

# Create your views here.

# 拆分页面
def TVCS_chai(request):
    return render(request,'myapp/page_two.html')
#合并页面
def TVCS_he(request):
    return  render(request,'myapp/page_one.html')











def index(request):
    # article = Article.objects.get(pk =1)#获取一个
    articles = Article.objects.all()#获取全部,返回列表
    # 参数，request，模板文件index.html,传递数据
    return render(request, "myapp/index.html", {'articles': articles})


def article_page(request,article_id):
    article = Article.objects.get(pk = article_id)
    return render(request,'myapp/article_page.html',{'article':article})

def article_edit(request,article_id):
    if str(article_id) == '0':
        return render(request, 'myapp/edit_article.html')
    article = Article.objects.get(pk=article_id)
    return render(request,'myapp/edit_article.html',{'article':article})

def edit_action(request):
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    article_id = request.POST.get('article_id',0)
    if str(article_id) == '0':
        #添加
        Article.objects.create(title=title,content=content)
        articles = Article.objects.all()  # 获取全部,返回列表
        return render(request, "myapp/index.html", {'articles': articles})
    article = Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'myapp/article_page.html', {'article': article})

def upload_html(request):
    return render(request,'myapp/upload_file.html')

def upload_file(request):
    import os
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("selectPictrue", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")

