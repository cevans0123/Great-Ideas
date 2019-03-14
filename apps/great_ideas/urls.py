from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index ),        #LOG/REG
    url(r'^login$', views.login),    #LOGIN
    url(r'^create$', views.create ), #this is the REG
    url(r'^ideas$', views.ideas ),  #ideas
    url(r'^(?P<id>\d+)$', views.view),  #View 
    url(r'^new$', views.new ),        #Add  TEMPLATE
    url(r'^add$', views.add),  #add  process
    url(r'^(?P<idea_id>\d+)/delete$', views.delete),  #Cancel
    url(r'(?P<id>\d+)/edit$', views.edit ), #EDIT 
    url(r'^(?P<id>\d+)/update$', views.update ),
    url(r'^(?P<idea_id>\d+)/like$', views.like),
    url(r'^logout_user$', views.logout_user),
]