from django.urls import path
from .views import home,Single_new

urlpatterns = [
    path('',home,name='home'),
    path('news/<int:year>/<int:month>/<int:day>/<slug:slug>',Single_new,name='single_new'),
]
