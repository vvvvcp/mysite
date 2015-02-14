from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.http import Http404
from django.core.urlresolvers import reverse

from polls.models import Question, Choice
import datetime

def index(request):
    return render(request,
                  'polls/index.html',
                  {'latest_question_list': Question.objects.order_by('-pub_date')})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def has_voted(request):
    return request.session.get('voted', 0)
#return 0

def register(request):
    return 'register page'

def vote(request, question_id):
    output = ''
    #for meta in request.META:
    #    line = "%s == \"%s\"<br/>\n" % (meta, request.META[meta])
    #    output += line
    #return HttpResponse(output)

    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        voted = has_voted(request)
        if not voted:
            selected_choice.votes += 1
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            request.session['voted'] = 1
            request.session.set_expiry(datetime.timedelta(days=7).seconds)
            return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        elif voted == -1:
            return HttpResponseRedirect(reverse('polls:register', args=(p.id,)))
        else: # voded == 1
            return render(request, 'polls/results.html', {
                'question': p,
                'error_message': "You have voted.",
            })

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'question': question})
