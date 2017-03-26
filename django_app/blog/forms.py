from django import forms


class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(
        widget=forms.Textarea
    )
