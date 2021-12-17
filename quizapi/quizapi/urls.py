from django.contrib import admin
from django.conf.urls import include, url
from polls.views import Index

urlpatterns = [
    url('polls/', include('polls.urls')),
    url('account/', include('account.urls')),
    url('admin/', admin.site.urls),
]
