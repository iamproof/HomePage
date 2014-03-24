from django.db import models
from django.contrib.auth.models import User
from django import forms
#from django.forms import ModelForm
from django.forms.extras.widgets import SelectDateWidget



# BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
BIRTH_YEAR_CHOICES = (range(1900,2014))
FAVORITE_COLORS_CHOICES = ( ('blue', 'Blue'),
                            ('green', 'Green'),
                            ('black', 'Black'),
                            ('red', 'Red'),
                            ('purple', 'Purple'),
                            ('pink', 'Pink'))
FAVORITE_MUSIC_CHOICES = (('alternative', 'Alternative'),
                          ('classical', 'Classical'),
                          ('country', 'Country'),
                          ('electronic', 'Electronic'),
                          ('house', 'House'),
                          ('metal', 'Metal'),
                          ('pop', 'Pop'),
                          ('rnb', 'RnB'),
                          ('rap', 'Rap'),
                          ('rock', 'Rock'))
SEX = (('female','Female'),
		('male', 'Male'))
FAVORITE_SPORTS_CHOICES = (('basketball', 'Basketball'),
                           ('football', 'Football'),
                           ('volleyball', 'Volleyball'),
                           ('swimming', 'Swimming'),
                           ('golf', 'Golf'),
                           ('snooker', 'Snooker'),
                           ('snowboard', 'Snowboard'),
                           ('ski', 'Ski'),
                           ('climbing', 'Climbing'))



class Info(models.Model):
    user = models.OneToOneField(User, unique=False)
    birth_year = models.DateField(blank=True, null=True)
    favorite_colors = models.CharField(max_length=150, choices=FAVORITE_COLORS_CHOICES, blank=True)
    favorite_music = models.CharField(max_length=150, choices=FAVORITE_MUSIC_CHOICES, blank=True)
    sex = models.CharField(max_length=150, choices=SEX, blank=True)
    favorite_sports = models.CharField(max_length=150, blank=True, null=True)
    about = models.TextField(blank=True)

    # def __str__(self):
    #   return self.user.username



class InfoForm(forms.Form): #forms.ModelForm): 
    birth_year = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES), required=False)
    favorite_music = forms.ChoiceField(widget=forms.RadioSelect,
                            choices=FAVORITE_MUSIC_CHOICES, required=False)
    favorite_colors = forms.ChoiceField(label='Favorite color',
        widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES, required=False)
    sex = forms.ChoiceField(widget=forms.RadioSelect,
    					    choices=SEX, help_text='A valid...', required=False)
    favorite_sports = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=FAVORITE_SPORTS_CHOICES)
    about = forms.CharField(widget=forms.Textarea, required=False)

    # class Meta:
    # 	model = Info
    # 	fields = ["birth_year", "favorite_music", "favorite_colors", "sex", "about"]