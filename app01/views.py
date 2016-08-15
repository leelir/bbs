from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from app01.models import Bbs, User_Comment, BBS_user

def index(request):
    bbs_list = Bbs.objects.all()
    print bbs_list
    return render_to_response('index.html',{'bbs_list': bbs_list,'user': request.user})

def bbs_detail(request, bbs_id):
    bbs = Bbs.objects.get(id = bbs_id)
    return render_to_response('bbs_detail.html', {'bbs': bbs})

@csrf_exempt
def sub_comment(request):
    try:
        bbs_id = request.POST.get('bbs_id')
        comment = request.POST.get('comment_content')
        User_Comment.objects.create(
                content_type_id = 7,
                site_id = 1,
                user = request.user,
                comment = comment,
                object_pk = bbs_id
        )
        return HttpResponseRedirect('/detail/%s' % bbs_id)
    except ValueError:
        return HttpResponse('please login at first.')

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html')

@csrf_exempt
def login_check(request):
    if request.method != 'POST':
        raise Http404('Only POST method allowed')
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/")
    else:
        # Show an error page
        return HttpResponse("error")


def logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

def bbs_pub(request):
    if request.user.is_authenticated():
        return render_to_response('bbs_pub.html')
    else:
        return render_to_response('login.html')

@csrf_exempt
def bbs_sub(request):
    bbs_content = request.POST.get('bbs_pub_content')
    author = BBS_user.objects.get(user__username = request.user)
    Bbs.objects.create(
        title = 'Test title',
        summary = 'Test summary',
        content = bbs_content,
        author = author,
        view_count = '1',
        ranking = '1'
    )
    return HttpResponseRedirect('/')
