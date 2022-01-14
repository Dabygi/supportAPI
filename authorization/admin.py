from django.contrib import admin
from authorization.models import UserManager, User, Profile


admin.site.register(UserManager)
admin.site.register(User)
admin.site.register(Profile)