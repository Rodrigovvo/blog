from typing import Any, Dict, Optional
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'is_active', 
        'is_staff', 'created_at', 'modified_at'
    )
    search_fields = ('email', 'first_name', 'last_name', )

    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save_and_add_another': False,
            'show_save_and_continue': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)

    def save_model(self, request, obj, form, change) -> None:
        obj.set_password(obj.password)
        return super().save_model(request, obj, form, change)

admin.site.register(User, UserAdmin)
