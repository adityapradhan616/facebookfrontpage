from django.contrib import admin
from socialapp.models import Userpost, UserProfile
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Userpost)