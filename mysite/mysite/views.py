import datetime
from django.http import HttpResponse,Http404
from django.template import Context
from django.template.loader import get_template

def hello(request):
    #ua  = request.META.get('HTTP_USER_AGENT','unkown')
    values = request.META.items()
    html = []
    for k,v in values:
        html.append('%s||||%s<br>' % (k, v))
    html.append(request.path)
    html.append(request.get_host())
    return HttpResponse(html)

def current_datetime(request):
    now  = datetime.datetime.now()
    # t  = get_template("current_date.html")
    # #raise False
    # html  = t.render({'current_date':now})
    # # html  = "<html><body>It is %s</body></html>" % now
    # return HttpResponse(html)
    from django.shortcuts import  render_to_response
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