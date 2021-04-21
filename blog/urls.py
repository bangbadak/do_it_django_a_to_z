from django.urls import path
from . import views

urlpatterns = [
    path('update_post/<int:pk>?', views.PostUpdate.as_view),
    path('create_psot/', views.PostCreate.as_view()),
    path('category/<str:slug>/', views.category),
    path('tag/<str:slug>/', views.tag_page),
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
    #path('', views.index),
    #path('<int:pk>', views.single_post_page),
]
