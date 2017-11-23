from django.conf.urls import url

from . import views

app_name = 'sexypic'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^meizi/$', views.meizi, name='meizi'),
    url(r'^pictrue/$', views.PicView.as_view(), name='pictrue'),
    url(r'^pictruedownload/$', views.pictruedownload, name='pictruedownload'),
]
