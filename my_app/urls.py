from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('edit/<int:pk>/',views.edit, name='edit'),
    path('delete/<int:pk>/',views.delete, name='delete'),
    path('add_item/',views.add_item, name='add_item'),
    path('view_item/<int:pk>/',views.view_item, name='view_item'),
]