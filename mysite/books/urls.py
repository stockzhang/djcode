from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # url(r'search-form',views.search_form),
    url(r'^$',views.thanks),
    url(r'search/$',views.search),
    url(r'contact/$',views.contact),
    url(r'contact/thanks/$',views.thanks),
    url(r'newtag/$',views.view_tag),
    url(r'about2/(?P<page>\w+)/$',views.AboutView2.as_view()),
    url(r'^about/',TemplateView.as_view(template_name="about.html"),{'TemplateDirect':'Temp'}),
]