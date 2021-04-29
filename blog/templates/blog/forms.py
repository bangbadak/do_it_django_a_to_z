from .models import Comment
from django import forms
class CommentForm(forms.ModelsForm):
    class Meta:
        model = Comment
        fields = ('content',)