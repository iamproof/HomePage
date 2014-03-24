from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):#admin.StackedInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question']
	fieldsets = [
		(None,                   {'fields': ['question']}),
		('Date information',     {'fields': ['pub_date']})   #, 'classes': ['collapse']})
		# (None,				 {'fields': ['author']}),
		]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date', 'question']
	search_fields = ['question']


admin.site.register(Poll, PollAdmin)