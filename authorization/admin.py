from django.contrib import admin
from authorization.models import User, Profile


admin.site.register(User)
admin.site.register(Profile)