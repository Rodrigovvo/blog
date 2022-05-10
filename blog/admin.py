from django.contrib import admin
from base.models import User
from django import forms
from .models import Post, Comment
from .forms import PostAdminForm


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'active', 'was_published')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'content',)
    form = PostAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "author":
            kwargs["queryset"] = User.objects.filter(pk=request.user.pk)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_author', 'content', 'post', 'like', 'dislike')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
