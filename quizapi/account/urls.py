from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^index/$', views.Index.as_view(), name="index"),
	url(r'^register/$', views.RegisterUser.as_view(), name="register"),
	url(r'^login/$', views.LoginUser.as_view(), name="login"),
	url(r'^logout/$', views.LogoutUser.as_view(), name="logout"),
]
