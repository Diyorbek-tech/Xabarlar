import datetime
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView, FormView, DeleteView, CreateView, UpdateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import News, Teg, Category
import requests

from .forms import UserRegisterform,Addnews


class Homeview(ListView):
    model = News
    context_object_name = "news"
    ordering = "-created_date"
    template_name = "base.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)

        text = "Urgench"
        api_url = f'https://api.weatherapi.com/v1/current.json?key=9e070c3df80441ffb0b113050232703&q={text}&aqi=no'
        data = requests.get(api_url)
        data = data.json()
        if len(data) > 1:
            loc = f"{data['location']['name']}"
            weather_data = f"{data['current']['temp_c']}"
            image = data['current']['condition']['icon']
            text = data['current']['condition']['text']
            data['loc'] = loc
            data['weather'] = weather_data
            data['weather_icon'] = image
            data['weather_text'] = text

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
    template_name = 'home-technology.html'


class Aboutview(TemplateView):
    template_name = 'page-about.html'


class Contactview(TemplateView):
    template_name = 'page-contact.html'


class Blogview(TemplateView):
    template_name = 'page-blog.html'


class Testformview(FormView):
    template_name = 'test.html'
    form_class = Addnews

    def post(self, request):
        if request.method == "POST":
            forms = Addnews(request.POST)
            if forms.is_valid():
                forms.save()
        return redirect('test')





