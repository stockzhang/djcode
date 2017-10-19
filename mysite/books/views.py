# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import  HttpResponse
from django.http import Http404
from django.template import TemplateDoesNotExist
from django.views.generic import TemplateView
from django.views.generic import  View
from models import book

#表单验证导入
from forms import ContactForm

def search_form(request):
    return  render_to_response('search_form.html')


def search(request):
    errors = []
    if 'q' in request.GET:
        # message  = 'You searched for: %r' % request.GET['q']
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 caracters.')
        else:
            books = book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',{'books':books,'query':q})
    return render_to_response('search_form.html',{'errors':errors})

#普通方式的contact表单验证
# def contact(request):
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject',''):
#             errors.append('Enter a subject.')
#         if not request.POST.get('message',''):
#             errors.append('Enter a message')
#         #raise False
#         if request.POST.get('email') and u'@' not in request.POST['email']:
#             errors.append('Enter a valid e-mail address.')
#         if not errors:
#             # send_mail(
#             #     request.POST['subject'],
#             #     request.POST['message'],
#             #     request.POST.get('email','noreply@example.com'),
#             #     ['siteowner@example.com'],
#             # )
#             return HttpResponseRedirect('/book/contact/thanks/')
#     return render_to_response('contact_form.html',
#                               {'errors':errors,
#                                'subject':request.POST.get('subject',''),
#                                'message':request.POST.get('message',''),
#                                'email':request.POST.get('email','')},
#             )

#使用表单框架的contact验证
def contact(request):
    if request.method  == 'POST':
        form  = ContactForm(request.POST)
        if form.is_valid():
            cd  = form.cleaned_data
            # send_mail(
            #     cd['subject'],
            #     cd['message'],
            #     cd.get('email','noreply@example.com'),
            #     ['siteowner@example.com',]
            # )
            return  HttpResponseRedirect('/book/contact/thanks/')
    else:
        form = ContactForm(initial={'subject':'I love you site!','email':'abc@example.com'})
    return  render_to_response('contact_form.html',{'form':form})

def thanks(request):
    return render_to_response('thanks.html')

def view_tag(request):
    return render_to_response('newtag.html',context={'data':'I am cut.','up':'Upper','home_link':'http://www.baidu.com/','home_title':'title'})

#通用视图
# def about_view(request,page):
#     try:
#         return TemplateView(request,template='about_%s.html' % (page,))
#     except TemplateDoesNotExist:
#         raise  Http404
class AboutView(TemplateView):
    template_name = "about_a.html"

class AboutView2(View):
    def get(self,request,*args,**kwargs):
        page  = kwargs['page']
        return render_to_response("about_%s.html" % page)

