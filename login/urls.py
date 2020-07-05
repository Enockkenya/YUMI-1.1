from django.urls import  include, re_path, path

from . import views
from django.contrib.auth import views as auth_views
app_name = 'login'
urlpatterns = [
	path('accounts/password_reset/',auth_views.PasswordResetView.as_view(template_name='login/password_reset.html'), name='password_reset'),
    path('accounts/change-password/', auth_views.PasswordChangeView.as_view(template_name='login/password_change.html'), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeView.as_view(template_name='login/password_change.html'), name='password_change_done'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'), name='password_reset_done'),
    path('accounts/password-reset-confirm/', auth_views.PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='login/password_reset_complete.html'), name='password_reset_complete'),
   
    re_path('login/', include([
        re_path(r'^login_modal$', views.login_modal),
        re_path(r'^login_redirect$', views.login_redirect, name='login_redirect'),
        re_path(r'^login$', views.login_authentication),
        re_path(r'^logout$', views.logout_authentication),

    ])),
    
            ]


