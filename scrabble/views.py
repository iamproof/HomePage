from django.shortcuts import render
import pickle
import itertools
from django import forms


def create_scrabble_dict():
	# Load dictionary from txt file.
	with open("wordsEn.txt") as sja:
			sja = sja.read()

	sja = sja.splitlines()

	# Creating empty dictionary
	data = {2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}}


	# Word segregation - our algorithm need to be fast, if we don't do that it will
	# search for results for 5 min. instead it will finad results
	# in 0.5 secund.(there is 109-110 thousand words in the dictionary)
	for i in sja:
		if len(i)==2:
			first_letter = i[0]
			if first_letter not in data[2]:
				data[2].update({first_letter: [i]})
			else:
				data[2][first_letter].append(i)
		elif len(i)==3:
			first_letter = i[0]
			if first_letter not in data[3]:
				data[3].update({first_letter: [i]})
			else:
				data[3][first_letter].append(i)
		elif len(i)==4:
			first_letter = i[0]
			if first_letter not in data[4]:
				data[4].update({first_letter: [i]})
			else:
				data[4][first_letter].append(i)
		elif len(i)==5:
			first_letter = i[0]
			if first_letter not in data[5]:
				data[5].update({first_letter: [i]})
			else:
				data[5][first_letter].append(i)
		elif len(i)==6:
			first_letter = i[0]
			if first_letter not in data[6]:
				data[6].update({first_letter: [i]})
			else:
				data[6][first_letter].append(i)
		elif len(i)==7:
			first_letter = i[0]
			if first_letter not in data[7]:
				data[7].update({first_letter: [i]})
			else:
				data[7][first_letter].append(i)

	# Complement our dictionary - unfortunately there aren't two letters words starting
	# by the letters:  "f", "j", "q"
	data[2].update({"f": []})
	data[2].update({"j": []})
	data[2].update({"q": []})

	# Writing our dictionary to file. From now on we are using only this file.
	with open("Example.data", mode = "wb") as plik:
		pickle.dump(data, plik)




class SearchForm(forms.Form):
	letters = forms.CharField(max_length=7)

# Function that we use on server to find words from given letters
def scrabble_words(search):
	words = dict()
	# path = os.getcwd()+"/scrabble/scrabble_words.data"
	with open("/var/lib/openshift/533495c2e0b8cd050b000051/app-root/runtime/repo/wsgi/openshift/scrabble/scrabble_words.data", mode = "rb") as plik:
		example = pickle.load(plik)

	letters = search
	letters = letters.lower()
	for n in range(2,len(letters)+1):
		perm = list(itertools.permutations(letters, n))
		perm = ["".join(i) for i in perm]
		nazwa = list(set([ i for i in perm if i in example[n][i[0]] ]))
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
