
from django.conf.urls import url
from crud import views



urlpatterns = [
    #/members/
    #url(r'^members/$', views.index, name='index'),
    
    url(r'^members/$', views.MemberList.as_view(), name='index'), #追加
    #/members/add/
    url(r'^members/add/$', views.edit, name='add'),
    #/members/edit/1/
    url(r'^members/edit/(?P<id>\d+)/$', views.edit, name='edit'),  
    #/members/delete/1/
    url(r'^members/delete/(?P<id>\d+)/$', views.delete, name='delete'),
    #/members/detail/1/
    url(r'^members/detail/(?P<id>\d+)/$', views.detail, name='detail'),
]
