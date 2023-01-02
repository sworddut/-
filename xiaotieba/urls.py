from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("mine/", views.mine,name="mine"),
    path("member/", views.member,name="member"),
    path("collection/", views.collection,name="collection"),
    path("follow/", views.follow,name="follow"),
    path("history/", views.history,name="history"),
    path("append/",views.append,name="append"),
    path("search/",views.search,name="search"),
    path("searchWork/",views.searchWork,name="searchWork"),
    path("search/searchWork/",views.searchWork,name="searchWork"),
]