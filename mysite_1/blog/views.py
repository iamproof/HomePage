from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from blog.models import Post, Comment, CommentForm
from django.contrib.auth.models import User
from django.contrib import messages


def index(request):
	# posts = Post.objects.all()
	posts = Post.objects.filter(published=True)
	return render(request, 'blog/index.html', {'posts': posts})

def detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	comments = Comment.objects.filter(post_name=slug).order_by('-created')[:5]
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data["title"]
			comment = form.cleaned_data["comment"]
			# author = form.cleaned_data["author"]
			form = form.save(commit=False)
			form.post_name = slug
			if request.user.is_authenticated():
				form.author = request.user
			else:
				messages.info(request, 'You need to have an account to post a comment.')
				return redirect('auth:index')
			# user = User.objects.get(username__exact=request.user.username)
			# form.author = user
			form.save()
			#form.author = request.user.username
			
			# return render(request, 'blog/detail.html', {'form': CommentForm(), 'post': post, 'comments': comments})
			# return render_to_response('blog/detail.html', {'form': CommentForm(), 'post': post, 'comments': comments})
			return redirect('blog:index')
	else:
		form = CommentForm()
	return render(request, 'blog/detail.html', {'form': form, 'post': post, 'comments': comments})


