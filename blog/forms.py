from django import forms

from ckeditor.widgets import CKEditorWidget

from .models import Comment, Post


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_author', 'content', 'post')
        widgets = {'post': forms.HiddenInput()}
