from django.shortcuts import render, redirect

# View에 Model(Post 게시글) 가져오기


from .models import Post


# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world")

# def home(request):
#     template = loader.get_template('app1/index.html')
#     return HttpResponse(template.render(request))

def home(request):
    return render(request, 'index.html')


def user(request):
    return render(request, 'user/user.html')


# 게시글 리스트를 반환할 함수
def board(request):
    # 모든 Post 를 가져와 postlist에 저장
    postlist = Post.objects.all()
    # 게시판 페이지를 열 때, 모든 Post인 postlist 도 같이 가져옴.
    return render(request, 'board/board.html', {'postlist': postlist})  # postlist 이름으로 postlist 객체를 전달.


# 해당 게시글 하나만 가져오는 함수
def posting(request, pk):
    # pk를 이용하여 하나의 게시글을 검색.
    post = Post.objects.get(pk=pk)
    return render(request, 'board/posting.html', {'post': post})


def write_posting(request):
    if request.method == 'POST':
        new_text = Post.objects.create(
            postname=request.POST['postname'],
            contents=request.POST['contents'],
        )
        return redirect('/board')

    return render(request, 'board/write_posting.html')
