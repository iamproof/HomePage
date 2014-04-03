from django.shortcuts import render

from urllib.request import Request
from urllib.request import urlopen
import re


def nba_news():
	request = Request('http://www.nba.com/news/')
	response = urlopen(request)
	http = str(response.read())
	urls = re.findall('<h3><a href="(.+?)</a></h3>', http)
	urlsdate = re.findall('"nbaNewsTime">(.+?)&nbsp(.+?)</div>', http)
	urlsdate1 = []
	for i in urlsdate:
		n = " ".join(i)
		urlsdate1.append(n)
	w = 0
	news = []
	try:
		for i in urls:
			if "news" in i:
				i = i.replace("\\", "")
				entry = re.split('">', "http://www.nba.com"+i)
				entry.append(urlsdate1[w])
				w = w + 1
				news.append(entry)
	except:
		pass
	return news


def stocks():
	spolki = [
	['INGBSK (ING)', 'PLBSK0000017'],
	['KGHM (KGH)', 'PLKGHM000017'],
	['TVN (TVN)', 'PLTVN0000017'],
	['PKNORLEN (PKN)', 'PLPKN0000018']
	]
	notowania = []

	for spolka in spolki:
		http = urlopen("http://www.gpw.pl/ajaxindex.php?action=GPWListaSp&start=quotationsTab&gls_isin="+spolka[1]+"&lang=PL").read()
		strhttp = str(http)
		regex = '<th>Kurs ostatni</th>[^.]*<td>(.+?)</td>[^.]*<th>Zmiana</th>'
		patter = re.compile(regex)
		result = re.findall(patter, strhttp)
		notowania.append( (spolka[0], result[0]) )
	return notowania


def index(request):
	news = nba_news()
	stock = stocks()
	return render(request, 'news/index.html', {"nba_news": news, "stock": stock})
