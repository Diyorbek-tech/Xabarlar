from django.urls import path
from .views import  Homeview, Singlenew,Technologyview,\
    Aboutview,Contactview,Blogview
from django.views.static import serve
from django.urls import re_path
from django.conf import settings

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path('', Homeview.as_view(), name='home'),
    path('testhome/', Homeview.as_view(), name='testhome'),
    path('news/<int:year>/<int:month>/<int:day>/<slug:slug>', Singlenew.as_view(), name='single_new'),
    path('category/<slug:cat_name>',  Homeview.as_view(), name='homefilter'),
    path('teg/<slug:teg>',  Homeview.as_view(), name='homefilterteg'),
    path('technology/',Technologyview.as_view(),name='tech'),
    path('about/',Aboutview.as_view(),name='about'),
    path('contact/',Contactview.as_view(),name='contact'),
    path('blog/',Blogview.as_view(),name='blog'),
]
