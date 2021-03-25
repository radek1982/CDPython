from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index),
    path('messages', views.post),
    path('comments/<int:msgid>', views.comment),
    path('reset', views.reset)
    
]