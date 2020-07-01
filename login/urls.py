from django.urls import  include, re_path
from . import views

app_name = 'login'

urlpatterns = [
    re_path('login/', include([
        re_path(r'^login_modal$', views.login_modal),
        re_path(r'^login_redirect$', views.login_redirect, name='login_redirect'),
        re_path(r'^login$', views.login_authentication),
        re_path(r'^logout$', views.logout_authentication),

    ]))
]

