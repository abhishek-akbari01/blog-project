from django.shortcuts import render,redirect
from django.http import HttpResponse
from yomdemo.models import Slider,Blogs,Category,Work,WorkCategory,Contact,User,AddBlogs,Comment
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail,BadHeaderError

def home(request):
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    # Blogs.objects.all().delete()
    slider=Slider.objects.all()
    category=Category.objects.all()
    return render(request,'index.html',{'slider':slider,'category':category,'user_info':user})

def services(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    return render(request,'services.html',{'category':category,'user_info':user})

def clients(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    return render(request,'clients.html',{'category':category,'user_info':user})

def blogGrid(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    return render(request,'blog-grid.html',{'category':category,'user_info':user})

def books(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    id = request.GET['id']
    blogs = Blogs.objects.filter(category=id)

    return render(request,'books.html',{'blogs':blogs,'category':category,'user_info':user})

def blogSingle(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    return render(request,'blog-single.html',{'category':category,'user_info':user})

def about(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    return render(request,'about.html',{'category':category,'user_info':user})

def column3(request):
    category=Category.objects.all()
    work = Work.objects.all()
    workcategory = WorkCategory.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    return render(request,'work-3columns.html',{'category':category,'work':work,'workcategory':workcategory,'user_info':user})

def column4(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    return render(request,'work-4columns.html',{'category':category,'user_info':user})

def singleProject(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    return render(request,'single-project.html',{'category':category,'user_info':user})

def contact(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact = Contact(
            name = name,
            email = email,
            subject = subject,
            message = message,
        )
        contact.save()

        if email:
            try:
                send_mail('Regarding visit our website','we will contact you soon!','abhiakbari971201@gmail.com',[email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return render(request,'contact.html',{'category':category,'name':name,'email':email,'subject':subject,'message':message,'user_info':user})
    else:
        return render(request,'contact.html',{'category':category,'user_info':user})

def register(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        user = User(
            name = name,
            email = email,
            password = password,
        )
        user.save()

        return render(request,'registrartion.html',{'category':category,'name':name,'email':email,'password':password,'user_info':user})
    else:
        return render(request,'registrartion.html',{'user_info':user,'category':category})

def login(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email=email,password=password)
        if user.count() ==1:
            row = user.get()
            request.session['user_id'] =row.id 
            return redirect('/')
        else:
            messages.add_message(request,messages.INFO,"EMail/Password is invalid")
            return redirect('/login')
    return render(request,'login.html',{'category':category,'user_info':user})

def logout(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    try:
      del request.session['user_id'] 
    except KeyError:
      pass
    if request.session.has_key('user_id'):
       user_id = request.session['user_id']
       user = User.objects.filter(id=user_id).get()
       user = None
       return render(request,'index.html',{'category':category,'user_info':user})
    return redirect('/')
#    return HttpResponse("<strong>You are logged out.</strong>")

def edit(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    edit_id = request.session['user_id']
    row = User.objects.filter(id=edit_id).get()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        r = User.objects.filter(id=edit_id)
        r.update(
            name = name,
            email = email,
            password = password,
        )
        return redirect('/register')
    return render(request,'registrartion.html',{'row':row,'category':category,'user_info':user})


def add_post(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None

    form = AddBlogs()
    if request.method == 'POST':
        form = AddBlogs(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse('WRONG')
    rows = Blogs.objects.all()
    return render(request,'add_post.html',{'form':form,'row':rows,'category':category,'user_info':user})


def view_post(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    user_id = request.session['user_id']
    row_id  = Blogs.objects.filter(user_id = user_id)
    return render(request,'view_post.html',{'row_id':row_id,'category':category,'user_info':user})
    
def delete_post(request):
    # user_id = request.session['user_id']
    # del_id = Blogs.objects.filter(user_id = user_id).get()
    del_id = request.GET['id']
    row = Blogs.objects.filter(id = del_id)
    row.delete()
    return redirect('/view_post')

def edit_post(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    edit_id = request.GET['id']
    row = Blogs.objects.filter(id = edit_id).get()
    category = Category.objects.all()

    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        name = request.POST['name']
        category = request.POST['category']
        image_name = FileSystemStorage().save(image.name,image)
        url = FileSystemStorage().url(image_name)

        r = Blogs.objects.filter(id=edit_id)
        r.update(
            name = name,
            category = category,
            image = url,
        )
        return redirect('/')
    return render(request,'edit_post.html',{'row':row,'category':category,'user_info':user})

def blog_single(request):
    category=Category.objects.all()
    if request.session.has_key('user_id'):
        user_id = request.session['user_id']
        user = User.objects.filter(id=user_id).get()
    else:
        user_id = 0    
        user = None
    id  = request.GET['id']
    blog = Blogs.objects.filter(id=id).get()
    recent_Post = Blogs.objects.all().order_by('-created_at')[:3]
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        fs = FileSystemStorage()
        filename = fs.save(image.name,image)
        uploaded_file_url = fs.url(filename)

        com = Comment(
            name = name,
            email = email,
            content = content,
            image = uploaded_file_url,
        )
        com.save()
        com_list = Comment.objects.all()
        return render(request,'blog-single.html',{'blog':blog,'recent_Post':recent_Post,'com_list':com_list,'category':category,'user_info':user})
    else:
        return render(request,'blog-single.html',{'blog':blog,'recent_Post':recent_Post,'category':category,'user_info':user})


# def mail_demo(request):
#     send_mail(
#         'this is my subject',
#         'Here is the message.',
#         'paresh.pampim@gmail.com',
#         ['abhishekakbari9668@gmail.com']
#     )
#     return HttpResponse("Good")

    
        

