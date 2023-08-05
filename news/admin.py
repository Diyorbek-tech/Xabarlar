from django.contrib import admin
from .models import News,Category,Teg,NewsContent
# Register your models here.


admin.site.register(News)
admin.site.register(Category)
admin.site.register(Teg)
admin.site.register(NewsContent)