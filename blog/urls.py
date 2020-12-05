from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("",views.index,name="home"),
    path("authors",views.authors,name="authors"),
    path("signin",views.signin,name="signin"),
    path("signout",views.signout,name="signout"),
    path("signin-action",views.signin_action,name="signin_action"),
    path("author-blogs/<int:id>",views.author_blogs,name="author_blogs"),
    path("new-article",views.new_article,name="new_article"),
    path("new-article-action",views.new_article_action,name="new_article_action"),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

