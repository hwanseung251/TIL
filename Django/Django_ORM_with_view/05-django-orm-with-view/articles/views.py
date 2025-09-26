from django.shortcuts import render, redirect
from .models import Article 

# Create your views here.

# 전체 게시글 조회(1) 후 메인 페이지 응답(2)
def index(request):
    # 1. DB에 전체 게시글을 조회
    articles = Article.objects.all()

    # 2. 전체 게시글 목록을 템플릿과 함께 응답
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 게시글 상세 페이지를 응답하는 함수
# 1. 몇번 게시글인지를 DB에 조회
# 2. 조회한 상세 게시글 데이터를 템플릿과 함께 응답
def detail(request, pk): # url에서 받은 pk이름과 같아야한다는 약속
    # 1. 단일 게시글 조회 
    # queryset API method ==> get() # 유일한 식별자를 조회하고싶을때는 get()!
    article = Article.objects.get(pk=pk) # 왼쪽의 pk는 Article모델의 컬럼 오른쪽의 pk는 인자로받은 pk

    # 2. 단일 게시글 데이터와 템플릿을 응답
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

# 사용자가 게시글 생성을 위한 작성 페이지를 응답하는 함수
def new(request):
    return render(request, 'articles/new.html')

# 1. 사용자로부터 입력 받은 데이터를 추출
# 2. 추출한 데이터를 데이터베이스에 저장
# 3. 저장이 완료되었다는 페이지를 응답
def create(request):
    # 1. 
    title = request.POST.get('title') # html에 name속성에 넣어놓은 key값 쓰면됨
    content = request.POST.get('content')

    # 2. DB에 저장
    # # 2.1 
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2.2 # 정비를 하고 저장을 하는 
    article = Article(title=title, content=content) 
    article.save()

    # # 2.3 # 유효성 검사 등이 불가능 
    # Article.objects.create(title=title, content=content)
    # return render(request, 'articles/create.html')

    # client한테 새로운 주소로 요청을 보내게끔 시켜야 함
    # return redirect('articles:index')
    return redirect('articles:detail', article.pk)

def delete(request, pk):
    # 1. 어떤 게시글 삭제할 건지 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회한 게시글을 삭제
    article.delete()

    # 3. 메인페이지로 리다이렉트
    return redirect('articles:index')

# 사용자에게 수정하는 form이 담긴 페이지를 응답
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')

    article.save()

    return redirect('articles:detail', article.pk)