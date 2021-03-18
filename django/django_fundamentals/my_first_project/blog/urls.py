from django.urls import path

from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('blogs', views.index, name="index"),
    path('blogs/new', views.new, name="new"),
    path('blogs/create', views.create, name="create"),
]