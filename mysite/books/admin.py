# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Publisher,Author,book

class AuthoAdmin(admin.ModelAdmin):
    #列表显示
    list_display = ('first_name','last_name','email')
    #search栏
    search_fields = ('first_name','last_name')

class bookAdmin(admin.ModelAdmin):
    #列表的显示
    list_display = ('title','publisher','publication_date')
    #过滤
    #list_filter = ('publication_date',)
    list_filter = ('title','publisher')
    #根据日志的过滤
    date_hierarchy = 'publication_date'
    #列表排序
    ordering = ('-publication_date',)
    #表单
    fields = ('title','authors','publisher','publication_date')
    #fields = ('title', 'authors', 'publisher')
    #针对多选多展现，水平展现
    filter_horizontal = ('authors',)
    #针对多对多展现，垂直展现
    #filter_vertical = ('authors',)
    #针对一对多展现
    raw_id_fields = ('publisher',)

admin.site.register(Publisher)
admin.site.register(Author,AuthoAdmin)
admin.site.register(book,bookAdmin)
