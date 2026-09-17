from django import forms
from blog.models import Comment


class Comment_form(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'subject', 'message']
