from django.contrib import admin
from .models import User,Appliance

admin.site.register(Appliance)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email','mobile','password')