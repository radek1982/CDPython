from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse

# Create your views here.

data = {"title": "My first blog", "content": "whatever"}

def root(req):
      return redirect("/blogs")

def index(req):
    return HttpResponse("placeholder to later display a list of all blogs with a method named index")


def new(req):
    return HttpResponse("placeholder for a new blog form")

def create(req):
    return redirect("/")

def show(req, blog_id):
    return HttpResponse("showing blog id " + str(blog_id)) 
def edit(req, blog_id):
    return HttpResponse("edit blog id " + str(blog_id)) 

def destroy(req, blog_id):
    return HttpResponse("delete blog id " + str(blog_id)) 

def json(req):
    return JsonResponse(data)