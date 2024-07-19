from django.urls import path
from quiz import views

urlpatterns = [
    path('',views.index, name="index"),
    path('addTask',views.addTask, name="addTask"),
    path('insert',views.insert_data, name="insert_data"),
    path('update/<int:id>',views.update_data, name="update_data"),
    path('delete/<int:id>',views.delete_data, name="delete_data"),
]