from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.ItemView.as_view(), name='item_view'),
    path('create_todo_item', views.item_create_view, name='item_create_view'),
]

