"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import logout
from Post.views import SignupView, Login, BlogView, HomeView, BlogPostView, MakeBlogPost


urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<slug>\w+)/$', BlogPostView.as_view(), name='myblog'),
    url(r'^post/(?P<id>\d{1,})/$', BlogView.as_view(), name='blogview'),
    url(r'^new-post/$', MakeBlogPost.as_view(), name='new-post'),

]
