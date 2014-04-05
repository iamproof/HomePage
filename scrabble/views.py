from django.shortcuts import render
import pickle
import itertools
from django import forms
# import os


class SearchForm(forms.Form):
	letters = forms.CharField(max_length=7)


def scrabble_words(search):
	words = dict()
	# path = os.getcwd()+"/scrabble/scrabble_words.data"
	#/var/lib/openshift/533495c2e0b8cd050b000051/app-root/runtime/repo/wsgi/openshift
	with open("/var/lib/openshift/533495c2e0b8cd050b000051/app-root/runtime/repo/wsgi/openshift/scrabble/scrabble_words.data", mode = "rb") as plik:
		example = pickle.load(plik)

	letters = search
	letters = letters.lower()
	for n in range(2,len(letters)+1):
		perm = list(itertools.permutations(letters, n))
		perm = ["".join(i) for i in perm]
		nazwa = list(set([i for i in perm if i in example[n-2]]))
		words[n] = nazwa

	return words





def index(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			letters = form.cleaned_data['letters']
			words = scrabble_words(letters)
			return render(request, "scrabble/index.html", {"form": form, "words": words})

	form = SearchForm()
	return render(request, "scrabble/index.html", {"form": form})
