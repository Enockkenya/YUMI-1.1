from django.urls import  include, re_path
from . import views

app_name = 'registration'

urlpatterns = [
    re_path('register/', include([
        re_path(r'^register_modal$', views.register_modal),
        re_path(r'^register$', views.register),
        re_path(r'^redirected_register$', views.redirected_register, name='redirected_register'),
    ]))
]

