from django.shortcuts import render
from django.contrib import messages

from polls.models import Poll, Choice
from blog.models import Post
from django.contrib.auth.models import User
import random

# Create your views here.

def index(request):
	n = random.randrange(0, 5)
	
	if n==0:
		messages.set_level(request, messages.DEBUG)
	elif n==1:
		messages.set_level(request, messages.INFO)
	elif n==2:
		messages.set_level(request, messages.SUCCESS)
	elif n==3:
		messages.set_level(request, messages.WARNING)
	elif n==4:
		messages.set_level(request, messages.ERROR)


	# Logged in User Name Info
	if request.user.username:
		name = 'Are You {}?'.format(request.user.username)
	else:
		name = "I don't know You! Can you please log in! I would like to know more about you."

	# request.META Info
	meta = "You are now using {}.".format(request.META['HTTP_USER_AGENT'])

	# Users Info
	how_many_users = len(User.objects.all())
	users = "We have {} registered users!".format(how_many_users)

	# Blog Info
	post_id = random.randrange(1, len(Post.objects.all())+1)
	blog_post = Post.objects.get(pk=post_id)

	# Polls Info
	pk_q = random.randrange(1, len(Poll.objects.all())+1)
	question = Poll.objects.get(pk=pk_q)
	number = random.randrange(0, len(question.choice_set.all()))
	votes = question.choice_set.order_by('-votes')[number]

	

	messages.debug(request, name)
	messages.info(request, meta)
	messages.success(request, users)
	messages.warning(request, 'Intrested in "{}" ? Read the blog !'.format(blog_post))
	messages.error(request, '{} {}. --> Disagree? Vote!'.format(question, votes))
	
	return render(request, 'flash_message/index.html')