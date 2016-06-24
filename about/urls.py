from django.conf.urls import url

from . import views

app_name = 'about'
urlpatterns = [
    #home-page
    url('^$', views.about, name='about'),
]
