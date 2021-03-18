from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('reset-session', views.reset, name="reset"),
    path('increment', views.increment)
]