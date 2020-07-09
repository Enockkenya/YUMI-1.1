from django.urls import re_path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'adverts'


urlpatterns = [
    re_path('Ads/', include([
        re_path(r'^post_ad/$', views.post_ad, name='post_ad'),
        re_path(r'^$', views.adverts_list, name='adverts_list'),
        re_path(r'^edit_ad/(?P<id>\d+)/$', views.update_post, name='update_post'), 
        re_path(r'^delete_ad/(?P<id>\d+)/$', views.delete_post, name='delete_post'), 
        re_path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.advert_detail, name='advert_detail'), 
        re_path(r'^(?P<category_slug>[-\w]+)/$', views.adverts_list_by_category, name='adverts_list_by_category'),
        re_path(r'^likead/(?P<id>\d+)/$', views.like_ad, name='like_ad')


 
   ]))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
