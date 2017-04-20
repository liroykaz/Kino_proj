from django.conf.urls import url
from films import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^films/(?P<pk>[0-9]+)/$', views.film, name="film")

    # url(r'^(?:(?P<id>\d+)/)?$', views.rub, name="rub"),
    # url(r'rubs/', views.rubs, name="rubs"),
    # url(r'author/', views.author, name="author"),
]