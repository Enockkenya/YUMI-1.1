from django.urls import  include, re_path
from account.views import mail
from account.views import profile
from account.views import setting
from account.views import *

app_name = 'account'

urlpatterns = [
    re_path('profile/', include([
        re_path(r'^send_email_message$', mail.email_users),
        re_path(r'^inbox$', mail.mail_page),
        re_path(r'^send_private_message$', mail.send_private_message),
        re_path(r'^view_private_message$', mail.view_private_message),
        re_path(r'^delete_private_message$', mail.delete_private_message),
  
        # re_path(r'^update_user$', profile.update_user),
        re_path(r'^settings$', setting.settings_page),
        re_path(r'^update_password$', setting.update_password),
        re_path(r'^update_profile$', profile.update_profile, name='update_profile'),
        
        re_path(r'^view_profile', profile.view_profile, name ='view_profile'),
        re_path(r'^view_my_ads/(?P<user_id>\d+)/$', profile.view_my_ads, name='view_my_ads'),
        re_path(r'^view_saved_ads$', profile.view_saved_ads, name='view_saved_ads'),
        re_path(r'^view_message$', profile.view_messages, name= 'view_messages'),
        re_path(r'^view_who_watched$', profile.view_who_watched, name='view_who_watched'),
        re_path(r'^view_settings$', profile.view_settings, name='view_settings'),

        ]))
]