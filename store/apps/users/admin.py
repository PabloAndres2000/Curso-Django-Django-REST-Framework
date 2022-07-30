
# Django
from django.contrib import admin

# Models
from store.apps.users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    User model admin.
    """

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'ip_address')
    list_display_link = ('email', 'first_name', 'last_name' )

