from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponseRedirect
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm


# Create your views here.
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request, *args, **kwargs):
    questions = Question.objects.order_by('-id')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'qa/index.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
        'title': "Latest questions"
    })


def popular_questions(request, *args, **kwargs):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'qa/index.html', {
        'posts': page.object_list,
        'paginator': paginator, 'page': page,
        'title': "Popular questions"
    })


def question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.clean()
            form.save()
            HttpResponseRedirect('/question/%s/' % question_id)
    else:
        form = AnswerForm()
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
        'form': form
    })


def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form.clean()
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})
