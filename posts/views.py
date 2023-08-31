from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-id')
    comment_form = CommentForm()

    context = {
        'posts': posts,
        'comment_form': comment_form,
    }
    return render(request, 'index.html', context)


@login_required # 로그인을 하지 않으면 실행하지 못함!
def create(request):
    if  request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
        

    context = {
        'form': form,
    }

    return render(request, 'form.html', context)

#댓글저장
@login_required
def comment_create(request, post_id):
    comment_form = CommentForm(request.POST)

    if comment_form.is_valid():
        comment = comment_form.save(commit=False)

        #현재 로그인 유저 넣기 > 로그인을 하지 않으면 에러남!
        comment.user = request.user
        # post_id를 기준으로 찾은 post(객체 이용)
        post = Post.objects.get(id=post_id)
        comment.post = post
        # 아이디 이용 가능
        # comment.post_id = post_id

        comment.save()
        return redirect('posts:index')
    
@login_required
def like(request, post_id):
    
    # 좋아요 버튼을 누른 유저
    user = request.user

    # 좋아요 버튼을 누른 게시물
    post = Post.objects.get(id=post_id)
    # user.like_posts.add(post)

    # 좋아요 버튼을 누른 경우
    if user in post.like_users.all():
        post.like_users.remove(user)
        # user.like_posts.remove(post)
    # 좋아요 버튼을 안 누른 경우 (좋아요 취소)
    else:
        post.like_users.add(user)

    return redirect('posts:index')