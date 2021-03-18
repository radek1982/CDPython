from django.urls import path

from . import views

urlpatterns = [
    path('', views.root, name='root'),
    path('blogs', views.index, name="index"),
    path('blogs/new', views.new, name="new"),
    path('blogs/create', views.create, name="create"),
    path('blogs/<int:blog_id>', views.show, name="show"),
    path('blogs/<int:blog_id>/edit', views.edit, name="edit"),
    path('blogs/<int:blog_id>/delete', views.destroy, name="destroy"),
    path('blogs/json', views.json, name="json")
    
]