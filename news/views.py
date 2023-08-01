import datetime
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import News, Teg, Category



class Homeview(ListView):
    model = News
    context_object_name = "news"
    ordering = "-created_date"
    template_name = "base.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        data['news'] = News.objects.all().order_by('-created_date')
        data['latest'] = News.objects.all().order_by('-created_date')[:10]
        data['time'] = datetime.datetime.now()
        data['breakingnews'] = News.objects.all().order_by('-created_date')[:5]
        data['tegs'] = Teg.objects.all()
        data['cats'] = Category.objects.all()
        data['tops'] = News.objects.all().order_by('-review')[:3]

        return data




class Singlenew(DetailView):
    model = News
    context_object_name = 'single'
    template_name = 'page-single-post-creative.html'

    def get(self, request, year, month, day, slug):
        obj = News.objects.get(created_date__year=year, created_date__month=month, created_date__day=day, slug=slug)
        context = {
            'single': obj
        }
        return render(request, 'page-single-post-creative.html', context)


class Technologyview(TemplateView):
    template_name ='home-technology.html'

class Aboutview(TemplateView):
    template_name = 'page-about.html'
class Contactview(TemplateView):
    template_name = 'page-contact.html'
class Blogview(TemplateView):
    template_name = 'page-blog.html'
