from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import AppUser


class AppUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', ]


class AppUserInline(admin.StackedInline):
    model = AppUser
 
 
class UserAdmin(UserAdmin):
    inlines = (AppUserInline, )
     
 
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.register(AppUser, AppUserAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)