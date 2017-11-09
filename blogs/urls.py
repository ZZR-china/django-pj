from django.conf.urls import url

from . import views

app_name = 'blogs'
urlpatterns = [
  url(r'^$', views.IndexView.as_view(), name='index'),
  url(r'^pdf/$', views.pdf, name='pdf'),
  url(r'^add/$', views.add, name='add'),
]