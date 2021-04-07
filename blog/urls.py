from django.urls import path
from . import views

urlpatterns = [
#    path('<int:pk>/', views.single_post_page),
#    path('', views.index),
    path('', views.index, name='index'),
    path('<int:pk>', views.single_post_page, name='single_post_page'),
]
