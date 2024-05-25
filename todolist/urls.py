from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.ItemView.as_view(), name='home_page'),
]
