import datetime
from django import  template
from ..models import book,Author


register  = template.Library()

def cut(value,arg):
    return value.replace(arg,'')

@register.filter(name='lower')
def lower(value):
    return  value.lower()

register.filter('cut',cut)

class CurrentTimeNode(template.Node):
    def __init__(self,format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return   now.strftime(self.format_string)

@register.tag(name='current_time')
def do_current_time(parse,token):
    try:
        tag_name,format_string = token.split_contents()
    except ValueError:
        msg  = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string[1:-1])

#register.tag('current_time',do_current_time)


class CurrentTimeNode2(template.Node):
    def __init__(self, format_string,var_name):
        self.format_string = str(format_string)
        self.var_name = var_name

    def render(self, context):
        now = datetime.datetime.now()
        context[self.var_name] = now.strftime(self.format_string)
        return ''

# @register.tag(name='get_current_time')
# def do_current_time2(parse,token):
#     try:
#         tag_name,format_string = token.split_contents()
#     except ValueError:
#         msg  = '%r tag requires a single argument' % token.split_contents()[0]
#         raise template.TemplateSyntaxError(msg)
#     return CurrentTimeNode2(format_string[1:-1])
@register.tag(name='get_current_time')
def do_current_time2(parse,token):
    import re
    try:
        tag_name,arg  = token.contents.split(None,1)
    except ValueError:
        msg = '%r tag requires arguments' % token.contents[0]
        raise template.TemplateSyntaxError(msg)
    m = re.search(r'(.*?) as (\w+)',arg)
    if m:
        fmt,var_name  = m.groups()
    else:
        msg = '%r tag had invalid arguments' % tag_name
        raise template.TemplateSyntaxError(msg)
    if not (fmt[0] == fmt[-1] and fmt[0] in ('"', "'")):
        msg = "%r tag's argument should be in quotes" % tag_name
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode2(fmt[1:-1],var_name)

@register.tag(name='upper')
def do_upper(parse,token):
    nodelist = parse.parse(('endupper',))
    parse.delete_first_token()
    return  UpperNode(nodelist)

class UpperNode(template.Node):
    def __init__(self,nodelist):
        self.nodelist  = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        return output.upper()

@register.inclusion_tag('thanks.html')
def books_for_author(author):
    books  = book.objects.all()
    return  {'books':books}

@register.inclusion_tag('link.html',takes_context=True)
def jump_link(context):
    return {'link':context['home_link'],'title':context['home_title']}