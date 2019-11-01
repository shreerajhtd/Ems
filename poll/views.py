from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from poll.models import *
from django.http import Http404, HttpResponse


def index(request):
    context = {}
    questions = Question.objects.all()
    context['title'] = 'polls'
    context['questions'] = questions
    return render(request, 'polls/index.html', context)

@login_required(login_url="/login/")
def detail(request, id = None):
    context = {}
    try:
        question = Question.objects.get(id=id)
    except:
        raise Http404
    context['question'] = question
    return render(request, 'polls/detail.html', context)

@login_required(login_url="/login/")
def poll(request, id = None):
    if request.method == "GET":
        try:
            question = Question.objects.get(id=id)
        except:
            raise Http404
        context = {}
        context['question'] = question
        return render(request, 'polls/poll.html', context)

    if request.method == "POST":
        user_id = 1
        data = request.POST
        ret = Answer.objects.create(user_id= user_id, choice_id= data['choice'])
        if ret:
            return HttpResponse("Your vote is done successfully")
        else:
            return HttpResponse("Your vote is not done successfully")


def poll_details(request, id = None):
    context = {}
    context['poll'] = get_object_or_404(User, id= id)
    return render(request, 'polls/detail.html', context)
