from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^detail/(?P<slug>[-\w]+)$', views.post_detail, name="detail"),
    url(r'^list/$', views.post_list, name="list"),
    url(r'^create/$', views.post_create, name="create"),
    url(r'^update/(?P<slug>[-\w]+)$', views.post_update, name="update"),
    url(r'^delete/(?P<slug>[-\w]+)$', views.post_delete, name="delete"),
    url(r'^home/$', views.post_home, name="home"),
    url(r'^eventcreate/$', views.event_create, name="eventcreate"),
    url(r'^eventlist/$', views.event_list, name="eventlist"),
    url(r'^eventdelete/(?P<event_slug>[-\w]+)$', views.event_delete, name="eventdelete"),
    url(r'^eventeupdate/(?P<event_slug>[-\w]+)$', views.event_update, name="eventupdate"),
    url(r'^signup/$', views.usersignup, name="signup"),
    url(r'^login/$', views.userlogin, name="login"),
    url(r'^logout/$', views.userlogout, name="logout"),


]
