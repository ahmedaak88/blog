from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^detail/(?P<post_id>\d+)$', views.post_detail, name="detail"),
    url(r'^list/$', views.post_list, name="list"),
    url(r'^create/$', views.post_create, name="create"),
    url(r'^update/(?P<post_id>\d+)$', views.post_update, name="update"),
    url(r'^delete/(?P<post_id>\d+)$', views.post_delete, name="delete"),
    url(r'^home/$', views.post_home, name="home"),
    url(r'^eventcreate/$', views.event_create, name="eventcreate"),
    url(r'^eventlist/$', views.event_list, name="eventlist"),
    url(r'^eventdelete/(?P<post_id>\d+)$', views.event_delete, name="eventdelete"),
    url(r'^eventeupdate/(?P<post_id>\d+)$', views.event_update, name="eventupdate"),


]
