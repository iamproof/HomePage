from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Post(models.Model):
	title = models.CharField(max_length=140)
	description = models.CharField(max_length=200)
	content = models.TextField()
	slug = models.SlugField()
	published = models.BooleanField(default=True)
	created = models.DateTimeField()
	author = models.ForeignKey(User)
	link = models.URLField(blank=True)
	link_description = models.CharField(max_length=140, blank=True)

	class Meta:
		ordering = ['-created']

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('blog.views.detail', args=[self.slug])

class Comment(models.Model):
	title = models.CharField(max_length=140)
	post_name = models.CharField(max_length=140)
	author = models.ForeignKey(User)# null=True, blank=True)
	comment = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ["title", "comment"]#, "author"]



