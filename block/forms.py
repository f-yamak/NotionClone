from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'body': CKEditorWidget()
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Untitled', 'style': 'color: black; border:none;'}),
        }
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'body': CKEditorWidget()
        }
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Untitled', 'style': 'width: 410px;'})
        }
