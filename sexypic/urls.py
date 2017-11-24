from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'sexypic'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^meizi/$', views.meizi, name='meizi'),
    url(r'^picture/$', views.PicView.as_view(), name='picture'),
    url(r'^picturedownload/$', views.picturedownload, name='picturedownload'),
    url(r'^snippets/$', views.snippet_list),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
