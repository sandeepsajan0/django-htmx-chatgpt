from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^$', views.hello),
    url(r'^home1/$', TemplateView.as_view(template_name='login_account/home1.html') ),
    url(r'^login_account/$', login , {'template_name': 'login_account/login1.html'}),
    url(r'^logout_account/$', logout , {'template_name': 'login_account/logout.html'}),
    url(r'^register/$',views.register),
    url(r'^profile/$',views.profile),
    url(r'^profile/edit/$',views.edit_profile),
    url(r'^public_page/$',views.BlogListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.post_detail, name='post_detail'),
    url(r'^post/new/$',views.news_poster, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.BlogUpdateView.as_view(), name='post_edit'),
    url(r'^author/(?P<pk>\d+)/delete/$',views.BlogDeleteView.as_view(), name='post_delete'),
     url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]

