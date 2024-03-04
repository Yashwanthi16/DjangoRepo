from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage,name = 'homepage'),
    path('display/', views.display_blogs, name='display_blog_data'),
    path('register/', views.enter_data, name='enter_blog_data'),
    path('describe_blog/<int:blog_id>/', views.describe_blog, name = 'specific_blog_details') ,
    path('search/', views.search, name='search')
    # this name field is used in url tag in index.html 
]

