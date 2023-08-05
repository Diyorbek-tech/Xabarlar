import string
import random

from django.db import models
from base.Base import BaseModel
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify

Regions = (
    ("Tashkent", "Tashkent"),
    ("Andijon", "Andijon"),
    ("Farg`ona", "Farg`ona"),
    ("Namangan", "Namangan"),
    ("Samarqand", "Samarqand"),
    ("Buxoro", "Buxoro"),
    ("Navoiy", "Navoiy"),
    ("Xorazm", "Xorazm"),
    ("Surxondaryo", "Surxondaryo"),
    ("Qashqadaryo", "Qashqadaryo"),
    ("Jizzax", "Jizzax"),
    ("Sirdaryo", "Sirdaryo"),
    ("Toshkent viloyat", "Toshkent viloyat"),
    ("Qoraqalpog`iston res", "Qoraqalpog`iston res"),
    ("Xorij", "Xorij"),

)


class Category(BaseModel):
    cat_name = models.CharField(max_length=60)

    def __str__(self):
        return self.cat_name


class Teg(BaseModel):
    tagname = models.CharField(max_length=30)

    def __str__(self):
        return self.tagname


class News(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=255)
    text = RichTextField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    teg = models.ManyToManyField(to=Teg)
    like = models.IntegerField(default=0)
    review = models.IntegerField(default=0)
    region = models.CharField(max_length=30, choices=Regions, default=Regions[0][0])

    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()  # bu-yangilik-bugun
        return super().save(*args, **kwargs)

    def generate_slug(self, save_to_obj=False, add_random_suffix=True):
        generated_slug = slugify(self.title)
        # Generate random suffix here.
        random_suffix = ""
        if add_random_suffix:
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(5)
            ])
            generated_slug += '-%s' % random_suffix

        if save_to_obj:
            self.slug = generated_slug
            self.save(update_fields=['slug'])

        return generated_slug

    def __str__(self):
        return self.title[:15]


class NewsContent(BaseModel):
    new = models.ForeignKey(to=News, on_delete=models.CASCADE)
    youtube_video_url = models.CharField(max_length=255, blank=True, null=True)
    other_video_url = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.CharField(max_length=255, blank=True, null=True)
    image_file = models.ImageField(upload_to="images/%Y/%m/%d/")

    def __str__(self):
        return self.new.title
