from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blog,Author
# Create your views here.


def index(request):
    if request.session.get("user") is not None:
        blogs = Blog.objects.all().order_by("-datetime")
        author_id = request.session.get("user")
        author = Author.objects.get(id=author_id)
        return render(request,"index.html",context={"author":author.name,"articles":blogs.values("id","datetime","title","blog_content","author__name","author__id","image")})
    else:
        return redirect("signin")

def authors(request):
    authors = Author.objects.all()
    return render(request,"authors.html",{"authors":authors})

def author_blogs(request,id):
    author = Author.objects.get(id=id)
    articles = Blog.objects.filter(author=author)
    return render(request,"index.html",{"articles":articles})

def new_article(request):
    print(request.session.get("user"))
    if request.session.get("user") is None:
        return redirect("signin")
    return render(request,"new-article.html")

def new_article_action(request):

    title = request.POST.get("title")
    content = request.POST.get("content")
    image = request.FILES["image"]
    author_id = request.session["user"]
    author = Author.objects.get(id=author_id)
    new_blog = Blog(title=title,blog_content=content,author=author,image=image)
    new_blog.save()
    return HttpResponse("Succesfully Added")

def signin(request):
    return render(request,"signin.html")

def signin_action(request):
    username = request.POST.get("email")
    password = request.POST.get("password")
    author_list = Author.objects.filter(username=username,password=password)
    if len(author_list) > 0:
        request.session["user"] = author_list.first().id
        return redirect("/")
    else:
        return HttpResponse("Signin failed !! :(")

def signout(request):
    print(request.session)
    del request.session["user"]
    return redirect("signin")