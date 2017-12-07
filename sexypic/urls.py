from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from . import controllers

app_name = 'sexypic'

viewpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^meizi/$', views.meizi, name='meizi'),
    url(r'^picture/$', views.PicView.as_view(), name='picture'),
    url(r'^picturedownload/$', views.picturedownload, name='picturedownload'),
]

restfulpatterns = [
    url(r'^snippets/$', controllers.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', controllers.SnippetDetail.as_view()),
    url(r'^users/$', controllers.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', controllers.UserDetail.as_view()),
]

urlpatterns = viewpatterns + restfulpatterns

urlpatterns = format_suffix_patterns(urlpatterns)
