from django.contrib import admin
from account.models import PrivateMessage, UserProfile


admin.site.register(PrivateMessage)
admin.site.register(UserProfile)
