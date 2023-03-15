from django.contrib import admin
from django.contrib.auth.models import Group

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'user_status',
        'created_at',
        'updated_at',
    )
    search_fields = ('email', 'username', )
    readonly_fields = ('id', 'created_at', 'updated_at')
    filter_horizontal = ()
    list_filter = ('created_at', 'updated_at')
    fieldsets = ()
    add_fieldsets = ()


admin.site.site_header = "Learning Management System"
admin.site.unregister(Group)
