from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'adverts'


urlpatterns = [
    url(r'^post_ad/$', views.view_post_ad, name='view_post_ad'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.advert_detail, name='advert_detail'), 
    url(r'^', views.adverts_list, name='adverts_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.adverts_list, name='adverts_list_by_category'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
