# -*- coding: utf-8 -*-

def deco_views(view):
    def inner(request,*args,**kwargs):
        return view(request,*args,**kwargs)
    return inner