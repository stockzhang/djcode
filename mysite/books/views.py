# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.http import  HttpResponse
from models import book

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

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject',''):
            errors.append('Enter a subject.')
        if not request.POST.get('message',''):
            errors.append('Enter a message')
        #raise False
        if request.POST.get('email') and u'@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            # send_mail(
            #     request.POST['subject'],
            #     request.POST['message'],
            #     request.POST.get('email','noreply@example.com'),
            #     ['siteowner@example.com'],
            # )
            return HttpResponseRedirect('/book/contact/thanks/')
    return render_to_response('contact_form.html',
                              {'errors':errors,
                               'subject':request.POST.get('subject',''),
                               'message':request.POST.get('message',''),
                               'email':request.POST.get('email','')},
            )

def thanks(request):
    return render_to_response('thanks.html')