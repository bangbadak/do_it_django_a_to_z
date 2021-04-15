from django.urls import path
from . import views

urlpatterns = [
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
    #path('', views.index),
    #path('<int:pk>', views.single_post_page),
]
