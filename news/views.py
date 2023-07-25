import datetime

from django.shortcuts import render
from django.http import HttpResponse
from .models import News,Teg,Category


def home(request):
    allnews=News.objects.all()
    alltegs=Teg.objects.all()
    allCat=Category.objects.all()

    context={
        "news":allnews,
        "tegs":alltegs,
        "cats":allCat,
    }

    return render(request,'home.html',context=context)


def Single_new(request,year,month,day,slug):
    date=datetime.datetime(year,month,day)
    anew=News.objects.get(slug=slug,created_date__year=year,created_date__month=month,created_date__day=day)
    context={
        'new':anew
    }
    return render(request,'single_news.html',context)

