from django.db import models
from base.Base import BaseModel
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

Regions=(
    ("Tashkent","Tashkent"),
    ("Andijon","Andijon"),
    ("Farg`ona","Farg`ona"),
    ("Namangan","Namangan"),
    ("Samarqand","Samarqand"),
    ("Buxoro","Buxoro"),
    ("Navoiy","Navoiy"),
    ("Xorazm","Xorazm"),
    ("Surxondaryo","Surxondaryo"),
    ("Qashqadaryo","Qashqadaryo"),
    ("Jizzax","Jizzax"),
    ("Sirdaryo","Sirdaryo"),
    ("Toshkent viloyat","Toshkent viloyat"),
    ("Qoraqalpog`iston res","Qoraqalpog`iston res"),
    ("Xorij","Xorij"),

)

class Category(BaseModel):
    cat_name=models.CharField(max_length=60)

    def __str__(self):
        return self.cat_name


class Teg(BaseModel):
    tagname = models.CharField(max_length=30)
    def __str__(self):
        return self.tagname


class News(BaseModel):
    title=models.CharField(max_length=255)
    slug=models.SlugField(unique=True,null=True,blank=True)
    text=RichTextField()
    category=models.ForeignKey(to=Category,on_delete=models.CASCADE)
    author=models.ForeignKey(to=User,on_delete=models.SET_NULL,null=True)
    teg=models.ManyToManyField(to=Teg)
    like=models.IntegerField(default=0)
    review=models.IntegerField(default=0)
    region=models.CharField(max_length=30,choices=Regions,default=Regions[0][0])



    def save(self,*args,**kwargs):
        self.slug=slugify(self.title) # bu-yangilik-bugun
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.title[:15]


