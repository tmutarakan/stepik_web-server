from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.http import require_GET
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, get_user
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm


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
            form._user = request.user
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
            form._user = request.user
            post = form.save()
            url = post.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form})


def check_login(login, password):
    try:
        user = User.objects.get(username=login)
    except Exception:
        return None
    if user.password != password:
        return None
    return user


def user_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = check_login(username, password)
        url = request.POST.get('continue', '/')
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(url)
        else:
            error = u'Неверный логин / пароль'

    return render(request, 'qa/login.html', {'form': LoginForm(), 'error': error })


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.clean()
            user = form.save()
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'qa/signup.html', {'form': form})
