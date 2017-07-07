from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^2003/$', views.special_case_2003),
    url(r'^(?P<year>[0-9]{4})/$', views.year_archive),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.article_detail),
]