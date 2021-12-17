from django.urls import path
from django.conf.urls import url

from . import views
#from views import Index, _AddPoll

urlpatterns = [
    url(r'^index/$', views.Index.as_view(), name="index"),
    url(r'^addpoll/$', views.AddPoll.as_view(), name="addpoll"),
    url(r'^vote/$', views.VotePoll.as_view(), name="vote"),
]
