# -*- coding: utf-8 -*-

def auth(get):
    def deco(func):
        def inner(*args,**kwargs):
            func(*args,**kwargs)
    return deco