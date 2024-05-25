from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
<<<<<<< HEAD
            'body': CKEditorWidget()
        }
        widgets = {
          'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Untitled', 'style': 'width: 410px;'})
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
=======
            'body': CKEditorWidget(),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Untitled', 'style': 'color: white; border:none;'}),
>>>>>>> e8573c0efacc3837e272acb553b569a615d21e63
        }
