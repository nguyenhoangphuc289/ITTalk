from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from apps.home import forms

from Core.BLL import *


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.user.is_authenticated():
        user = request.user
        name = user.first_name + " " + user.last_name
        context = {
            'name': name
        }
        return render(request, 'home/index.html', context)
    return render(request, 'home/index.html', "")


def login(request):
    return render(request, 'home/login.html', "")


@login_required(login_url='/login/')
def logout(request):
    auth_logout(request)
    return redirect('/')


@login_required(login_url='/login/')
def question(request):
    return render(request, 'home/question.html', "")


@login_required(login_url='/login/')
def detail(request, pid):
    topics = [
        'Python',
        'Django',
        'Open source',
        'Pycharm'
    ]
    postOrQuestion = PostBLL.SelectById(pid)
    context = {
        'topics': topics,
        'title': postOrQuestion.title,
        'content': postOrQuestion.content,
        'type_id': postOrQuestion.type_id
    }
    return render(request, 'home/detail.html', context)


@login_required(login_url='/login/')
def question_insert(request):
    title = str(request.POST['question_title'])
    isAnonymous = False
    if request.POST.get('is_anonymous', True) == "on":
        isAnonymous = True
    isExpand = request.POST['is_expand']
    content = request.POST['question_detail']
    userId = request.user.id
    if (isExpand == "1"):
        PostBLL.Insert(1, [], title, content, userId, isAnonymous)
    else:
        PostBLL.Insert(1, [], title, "", userId, isAnonymous)

    # NotificationBLL.create_notification(userId)

    return redirect('/detail/' + str(PostBLL.SelectLastQuestion(userId).id))


def schedule(request):
    return render(request, "home/schedule.html", "")


@login_required(login_url='/login/')
def post(request):
    return render(request, "home/post.html", {'form': forms.PostForm})


@login_required(login_url='/login/')
def post_insert(request):
    title = request.POST['title']
    content = request.POST['content']
    userId = request.user.id
    PostBLL.Insert(2, [], title, content, userId, 0)

    # NotificationBLL.create_notification(userId)

    return redirect('/detail/' + str(PostBLL.SelectLastPost(userId).id))


def ajax_load_more(request):
    if request.is_ajax():
        total = 1
        offset = int(request.GET.get('offset', '0'))
        end = offset + total
        template = 'home/load_more_items.html'
        if (offset < len(PostBLL.SelectAll())):
            feeds = PostBLL.SelectWithoutDownvotePost(request.user.id)[offset:end]
            data = {
                'logged_user_id': request.user.id,
                'posts': feeds,
            }
            return render_to_response(template, data)
        else:
            return render_to_response(template, None)


def ajax_delete_post(request):
    if request.is_ajax():
        PostBLL.Delete(request.GET.get('id', '0'))
    return HttpResponse()


def ajax_downvote_post(request):
    if request.is_ajax():
        PostBLL.IncreaseDownVote(request.GET.get('id', '0'), request.user.id)
    return HttpResponse()


def ajax_undo_downvote_post(request):
    if request.is_ajax():
        PostBLL.DecreaseDownvote(request.GET.get('id', '0'), request.user.id)
    return HttpResponse()
