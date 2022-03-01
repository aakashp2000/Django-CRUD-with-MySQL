from django.urls import path, include
from apps.crud import views

urlpatterns = [
    path('hello/', views.hello),
    path('get-tutorials/',views.get_tutorials),
    path('delete-tutorial/',views.delete_tutorial),
    path('update_tutorial/', views.delete_tutorial)

     ]