from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^makeentry/', views.makeentry),
    url(r'^$',views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='detail'),

]