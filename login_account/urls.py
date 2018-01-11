from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout
urlpatterns = [
    url(r'^$', views.hello),
    url(r'^login_account/$', login , {'template_name': 'login_account/login1.html'}),
    url(r'^logout_account/$', logout , {'template_name': 'login_account/logout.html'}),
    url(r'^register/$',views.register),
    url(r'^profile/$',views.profile),
    url(r'^profile/edit/$',views.edit_profile),
    url(r'^public_page/$',views.BlogListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.BlogDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$',views.news_poster, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.BlogUpdateView.as_view(), name='post_edit'),
    url(r'^author/(?P<pk>\d+)/delete/$',views.BlogDeleteView.as_view(), name='post_delete'),
]

