from django.urls import path
from . import views
from Hello import views

urlpatterns = [
    path('profile/<username>', views.profile), # url path for profile and username
    path("author/",views.ListAuthorAPIView.as_view(),name="Author_list"), #url path for list of author
    path("author/create/", views.CreateAuthorAPIView.as_view(),name="Author_create"), #url path to create author
    path("book/",views.ListBookAPIView.as_view(),name="Book_list"), #url path for list of book
    path("book/create/", views.CreateBookAPIView.as_view(),name="Book_create"), #url path to create book
]