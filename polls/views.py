#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Choice, Poll


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        return Poll.objects.published()[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Poll.objects.published()


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'

    def get_queryset(self):
        return Poll.objects.published()


def vote(request, slug):
    p = get_object_or_404(Poll.objects.published(), slug=slug)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.slug,)))
