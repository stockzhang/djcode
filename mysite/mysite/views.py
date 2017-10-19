import datetime
from django.http import HttpResponse,Http404
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
