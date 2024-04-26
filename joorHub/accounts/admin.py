from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Optionally customize the forms or list display here

admin.site.register(CustomUser, CustomUserAdmin)
