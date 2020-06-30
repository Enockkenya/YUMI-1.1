from django.conf.urls import  include, url
from account.views import mail
from account.views import profile
from account.views import setting
from account.views import *

app_name = 'account'

urlpatterns = [
    url(r'^send_email_message$', mail.email_users),
    url(r'^inbox$', mail.mail_page),
    url(r'^send_private_message$', mail.send_private_message),
    url(r'^view_private_message$', mail.view_private_message),
    url(r'^delete_private_message$', mail.delete_private_message),
    url(r'^profile$', profile.profile_page),
    # url(r'^update_user$', profile.update_user),
    url(r'^settings$', setting.settings_page),
    url(r'^update_password$', setting.update_password),
    url(r'^update_profile$', profile.update_profile, name='update_profile'),
    # url(r'^view/profile/profile/$', profile.view_profile, name ='view_profile'),
    url(r'^view_my_ads/(?P<user_id>\d+)/$', profile.view_my_ads, name='view_my_ads'),
    url(r'^view_saved_ads$', profile.view_saved_ads, name='view_saved_ads'),
    url(r'^view_message$', profile.view_messages, name= 'view_messages'),
    url(r'^view_favourite$', profile.view_favourite, name='view_messages'),
    url(r'^view_settings$', profile.view_settings, name='view_settings'),

]