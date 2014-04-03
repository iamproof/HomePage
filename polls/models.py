from django.db import models
import datetime
from django.utils import timezone
import random

# from django.contrib.auth.models import User      # addition to author

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # author = models.ForeignKey(User)

    def __str__(self):
    	return self.question

    def was_published_recently(self):
    	now = timezone.now()
    	return now - datetime.timedelta(days=1) <= self.pub_date <  now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def pro(self):                                    # Do usuniecia
        return random.random()

class Choice(models.Model):
    poll = models.ForeignKey(Poll)                    # Many-to-one relationships
#   poll = models.ManyToManyField(Poll)                 Many-to-many relationships
#   poll = models.OneToOneField(Poll)                   One-to-one relationships
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
    	return self.choice_text