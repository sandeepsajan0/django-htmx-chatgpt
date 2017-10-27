from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login
urlpatterns = [
    url(r'^$', views.hello),
    url(r'^login_account/$', login , {'template_name': 'login_account/login1.html'}),
    url(r'^register/$',views.register),
    url(r'^profile/$',views.profile),
    url(r'^profile/edit/$',views.edit_profile)
]
