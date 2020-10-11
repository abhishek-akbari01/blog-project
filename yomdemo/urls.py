from django.contrib import admin
from django.urls import path
from yomdemo.views import home,services,clients,blogGrid,blogSingle,about,column3,column4,contact,singleProject,books,register,login,logout,edit,add_post,view_post,delete_post,edit_post,blog_single
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home),
    path('home/',home),
    path('services/',services),
    path('clients/',clients),
    path('blog-grid/',blogGrid),
    path('category/',books),
    path('blog-single/',blogSingle),
    path('about/',about),
    path('column3/',column3),
    path('column4/',column4),
    path('singleProject/',singleProject),
    path('contact/',contact),
    path('register/',register),
    path('login/',login),
    path('logout/',logout),
    path('edit/',edit),
    path('add_post/',add_post),
    path('view_post/',view_post),
    path('delete/',delete_post),
    path('edit_post/',edit_post),
    path('blog_single/',blog_single),
    
   
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)