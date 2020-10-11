from django.contrib import admin
from yomdemo.models import Slider,Category, Blogs,Work,WorkCategory
# Register your models here.

admin.site.register([Slider,Category,Blogs,Work,WorkCategory])