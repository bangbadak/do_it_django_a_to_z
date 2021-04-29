from django.urls import path
from . import views

urlpatterns = [
    path('search/<str:q>/', views.PostSearch.as_view()),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_post/<int:pk>?', views.PostUpdate.as_view),
    path('create_psot/', views.PostCreate.as_view()),
    path('category/<str:slug>/', views.category),
    path('<int:pk>/new_comment/', views.new_comment()),
    path('tag/<str:slug>/', views.tag_page),
    path('<int:pk>/', views.single_post_page),
    path('', views.index),
    #path('', views.index),
    #path('<int:pk>', views.single_post_page),
]
