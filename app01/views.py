from datetime import datetime
import time

from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from app01.models import Bbs, User_Comment, BBS_user, Category

def index(request):
    bbs_uptime = []
    bbs_list = Bbs.objects.all()
    bbs_lee_list = Bbs.objects.filter(author_id = 1)
    bbs_category = Category.objects.all()
    for bbs in bbs_list:
        bbs.updated_at = datetime.fromtimestamp(time.mktime(bbs.updated_at.timetuple()) + 28800)
    return render_to_response('index.html',{
                            'bbs_list': bbs_list,
                            'bbs_lee_list': bbs_lee_list,
                            'user': request.user,
                            'category':bbs_category,
                            'cate_id': 0})

def category(request, cate_id):
    bbs_list = Bbs.objects.filter(category__id = cate_id)
    bbs_lee_list = Bbs.objects.filter(author_id = 1)
    bbs_category = Category.objects.all()
    return render_to_response('index.html',{
                            'bbs_list': bbs_list,
                            'bbs_lee_list': bbs_lee_list,
                            'user': request.user,
                            'category':bbs_category,
                            'cate_id': int(cate_id)})

def bbs_detail(request, bbs_id):
    bbs = Bbs.objects.get(id = bbs_id)
    bbs_category = Category.objects.all()
    bbs_uptime = datetime.fromtimestamp(time.mktime(bbs.updated_at.timetuple()) + 28800)
    return render_to_response('bbs_detail.html', {'bbs': bbs,'user': request.user,
    'category':bbs_category,'bbs_uptime': bbs_uptime})

@csrf_exempt
def sub_comment(request):
    try:
        bbs_id = request.POST.get('bbs_id')
        comment = request.POST.get('comment_content')
        User_Comment.objects.create(
                content_type_id = 11,
                # local content_type_id = 7
                # server content_type_id = 11
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
        bbs_category = Category.objects.all()
        return render_to_response('bbs_pub.html',{'user': request.user,'category':bbs_category})
    else:
        return render_to_response('login.html')

@csrf_exempt
def bbs_sub(request):
    bbs_title = request.POST.get('bbs_pub_title')
    bbs_category = request.POST.get('bbs_pub_cate')
    bbs_content = request.POST.get('bbs_pub_content')
    author = BBS_user.objects.get(user__username = request.user)
    Bbs.objects.create(
        title = bbs_title,
        summary = bbs_content,
        content = bbs_content,
        author = author,
        view_count = '1',
        ranking = '1',
        category_id = bbs_category
    )
    return HttpResponseRedirect('/')
