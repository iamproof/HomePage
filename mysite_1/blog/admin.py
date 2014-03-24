from django.contrib import admin
from blog.models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	fields = ['title', 'description',
			  'content', 'slug',
			  'published', 'created',
			  'author', 'link',
			  'link_description'
			  ]
	prepopulated_fields = {"slug": ("title",)}

	list_display = ('title', 'author', 'created','published')

admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
	fields = ['title', 'post_name', 'author', 'comment']
	list_display = ('title', 'author', 'created', 'post_name')
	list_filter = ['author', 'post_name', 'created']
	#pass

admin.site.register(Comment, CommentAdmin)
