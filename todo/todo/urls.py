from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.signup, name='signup'),
    path('loginn/', views.loginn, name='loginn'),
    path('todopage/', views.todo, name='todo_page'),
    path('edit_todo/<int:srno>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:srno>/', views.delete, name='delete'),
    path('complete/<int:srno>/', views.complete, name='complete'),
]