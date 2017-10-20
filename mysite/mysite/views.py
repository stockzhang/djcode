# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import Context,loader,RequestContext,Template
from django.template.loader import get_template
from django.shortcuts import render_to_response,render
#from books.authdeco import deco_views


def hello(request):
    #ua  = request.META.get('HTTP_USER_AGENT','unkown')
    values = request.META.items()
    html = []
    for k,v in values:
        html.append('%s||||%s<br>' % (k, v))
    html.append(request.path)
    html.append(request.get_host())
    return HttpResponse(html)

#@deco_views
def current_datetime(request):
    now  = datetime.datetime.now()
    # t  = get_template("current_date.html")
    # #raise False
    # html  = t.render({'current_date':now})
    # # html  = "<html><body>It is %s</body></html>" % now
    # return HttpResponse(html)
    return  render_to_response("current_date.html",{'current_date':now})

def hours_ahead(request,offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt  = datetime.datetime.now() + datetime.timedelta(hours=offset)
    t = get_template("hours_ahead.html")
    html = t.render({"hours_offset":offset,"next_time":dt})
    # raise  False
    #html  = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset,dt)
    return HttpResponse(html)

def custom_proc(request):
    return {
        'app': 'My app',
        'user': request.user,
        'ip_address': request.META['REMOTE_ADDR']
    }

def view1(request):
    t = loader.get_template('view1.html')
    return render(request,'view1.html',context={'message':'I am view1.'})
    # c = Context({
    #     'app':'My app',
    #     'user':request.user,
    #     'ip_address':request.META['REMOTE_ADDR'],
    #     'message':'I am the s view 1.'
    # }
    # )
    # return  t.render({
    #     'app':'My app',
    #     'user':request.user,
    #     'ip_address':request.META['REMOTE_ADDR'],
    #     'message':'I am the s view 1.'
    # })
    #return render_to_response('view1.html',{'app':'My app','user':request.user,'ip_address':request.META['REMOTE_ADDR'],'message':'I am view 1'})
    # t  = Template('{{ title }}:{{ ip_address }}')
    # c =  RequestContext(request,{'title':'Your IP Address'},[custom_proc])
    # # c = RequestContext(request,{'message':'I am view 1.'},[custom_proc])
    # raise  False
    # return HttpResponse(t.render(c))

def view2(request):
    t = loader.get_template('view2.html')
    # c = Context({
    #     'app':'My app',
    #     'user':request.user,
    #     'ip_address':request.META['REMOTE_ADDR'],
    #     'message':'I am the s view 1.'
    # }
    # )
    # return  t.render({
    #     'app':'My app',
    #     'user':request.user,
    #     'ip_address':request.META['REMOTE_ADDR'],
    #     'message':'I am the s view 1.'
    # })
    return HttpResponse(t.render({'app':'My app','user':request.user,'ip_address':request.META['REMOTE_ADDR'],'message':'I am view 2'}))

def showpic(request):
    import os
    from django.conf import  settings
    image_data = open(os.path.join(settings.BASE_DIR,r'mysite\templates\pic\fp.jpg'),'rb').read()
    return HttpResponse(image_data,content_type='image/png')

def showcsv(request):
    import csv
    UNRULY_PASSENGERS = [146, 184, 235, 200, 226, 251, 299, 273, 281, 304, 203]
    response  = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename=unruly.csv'
    writer  = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])
    return  response

#cookie
def show_color(request):
    if "favorite_color" in request.COOKIES:
        return  HttpResponse("You favorite color is: %s") % request.COOKIES['fovarite_color']
    else:
        return HttpResponse("You dont have a favorite color")

def set_color(request):
    # if 'favorite_color' in request.GET:
    #     response = HttpResponse('You favorite color is now %s' % request.GET['favorite_color'])
    #     response.set_cookie('fovarite_color',request.GET['favorite_color'])
    #     return  response
    # else:
    #     return HttpResponse('You didnt give a favorite color.')
    request.session['member_id']=101
    return HttpResponse('You set member id.')

from django.contrib.auth.decorators import login_required
@login_required(login_url='/register/')
def login_after_view(request):
    # if request.user.is_authenticated():
    #     return  HttpResponse("%s:login." % request.user)
    # else:
    #     return  HttpResponseRedirect("/admin/login/?next=%s" % request.path)
    return HttpResponse("%s:login." % request.user)

#注册表单
from django import  forms
from django.contrib.auth.forms import UserCreationForm
def register(request):
    if request.method  == 'POST':
        form  = UserCreationForm(request.POST)
        if form .is_valid():
            new_user  = form.save()
            return HttpResponseRedirect('/book/')
    else:
        form = UserCreationForm()
    return render_to_response('reg/register.html',{'form':form})