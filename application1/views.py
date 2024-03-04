from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Blog

# Create your views here.
#used for request and response

def homepage(request):
    return render(request,"index.html")

def display_blogs(request):
    post = Blog.objects.all()
    return render(request, "blogs_display.html", {'post':post})

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
    return render(request, "form.html")

#describing each blog in detail
def describe_blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "specific_blog_detail.html",{'blog':blog})


#searching based on title or author entered
def search(request):
    query = request.GET.get('q')
    if query:
        # Perform case-insensitive search on title and author fields
        results = Blog.objects.filter(title__icontains=query) | Blog.objects.filter(author__icontains=query)
    else:
        results = Blog.objects.none()
    return render(request, 'search_results.html', {'results': results})