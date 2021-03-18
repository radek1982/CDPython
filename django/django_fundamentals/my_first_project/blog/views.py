from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def root(req):
      return redirect("/blogs")

def index(req):
    return HttpResponse("placeholder to later display a list of all blogs with a method named index")


def new(req):
    return HttpResponse("placeholder for a new blog form")

def create(req):
    return redirect("/")
    