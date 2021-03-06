from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Poll, Choice

from django.views import generic

from django.utils import timezone


# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

    # render() function takes the request object as its first argument,
    # a template name as its second argument and a dictionary
    # as its optional third argument

def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    decreasing_poll = poll.choice_set.order_by('-votes')
    lista = poll.choice_set.all()
    average = len(lista) * [(sum([i.votes for i in lista]) ) / (len(lista))]
    return render(request, 'polls/results.html', {'poll': poll, 'decreasing_poll': decreasing_poll, 'lista': lista, 'average': average})

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)  # gets the object with the primary key of poll_id from Poll
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
        	'poll': p,
        	'error_message': "You didn't select a choice.",
            })
	# Redisplay the poll voting form.
	else:
		selected_choice.votes += 1
		selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))   