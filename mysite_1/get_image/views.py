from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django import forms

from urllib.request import Request
from urllib.request import urlopen
import re
import random

class SearchForm(forms.Form):
	search = forms.CharField(max_length=100)

def getpicWallbase(search):
	search = search.replace(" ","%20")
	request = Request("http://wallbase.cc/search?q=" + search)
	response = urlopen(request)
	http = str(response.read())
	partialurl = re.findall('http://wallbase.cc/wallpaper/(.+?)"', http)
	string= "http://wallpapers.wallbase.cc/rozne/wallpaper-"
	url = [string+i+".jpg" for i in partialurl]
	goodurls = []
	for i in url:
		try:
			urlopen(Request(i))
			goodurls.append(i)
			if len(goodurls) == 6:
				return random.sample(goodurls, 3)

		except:
			pass
	#url = [i for i in url if urlopen(Request(i))]
	#return random.sample(goodurls, 3)
	#return random.choice(url)

def index(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			search = form.cleaned_data['search']
			#return HttpResponseRedirect( getpicWallbase(search) )
			pictures = getpicWallbase(search)
			return render(request, 'get_image/index.html', {'form': form, 'pictures': pictures})
	else:
		form = SearchForm()
		
	return render(request, 'get_image/index.html', {'form': form})