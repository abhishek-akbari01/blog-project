from django.db import models
from django import forms


class Slider(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slides = models.FileField(upload_to='slider/')
    objects=models.Manager

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager

    def __str__(self):
        return self.title

class WorkCategory(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager 
    def __str__(self):
        return self.title

class Work(models.Model):
    image= models.FileField(upload_to='images/')
    category = models.ForeignKey(WorkCategory,on_delete = models.CASCADE) 
    title = models.CharField(max_length=100)
    content = models.TextField()
    objects = models.Manager
    def __str__(self):
        return self.category

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    objects = models.Manager

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    objects = models.Manager
    def __str__(self):
        return self.name

class Blogs(models.Model):
    image = models.FileField(upload_to='blog-image/')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,default="block")
    objects = models.Manager 

class AddBlogs(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ["image","name","category",'user'] 

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['user'].widget.attrs.update({'style': 'display:none'})
     
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.FileField(upload_to='comment-image/')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    objects = models.Manager

    