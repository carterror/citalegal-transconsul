from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    titulo = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    cuerpo = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    presentar = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))
    autor = forms.Select(attrs={"class": "form-select"})
    
    class Meta():
        fields = ['titulo', 'cuerpo', 'presentar', 'autor']
        model = Post