from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.
#used for request and response

def say_hello(request):
    post = Blog.objects.all()
    return render(request, "base.html", {'post':post})

#writing the form data to DB
def enter_data(request):
    if request.method == 'POST':
        title=request.POST['title']
        image=request.FILES.get('image')
        video=request.FILES.get('video')
        description=request.POST['description']
        author=request.POST['author']
        created_at=request.POST['created_at']

        obj = Blog(title=title, image=image, video=video, description=description, author=author, created_at=created_at)
        obj.save()
    return render(request, "demo.html")


