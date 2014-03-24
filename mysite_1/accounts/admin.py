from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from accounts.models import Info

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class InfoInline(admin.StackedInline):
    model = Info
    can_delete = False
    verbose_name_plural = 'Info' #Blue description

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (InfoInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
