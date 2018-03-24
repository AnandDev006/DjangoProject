from django import forms

class BlogForm(forms.Form):
    blogName = forms.CharField( max_length = 20,
        widget = forms.TextInput( attrs = {
            'class': 'form-control',
            'placeholder': 'Title',
            'id': 'inputname'
            } )
    )
    blogBody = forms.CharField(
        widget = forms.Textarea( attrs = {
        'class': 'form-control',
        'id': 'comment',
        'rows': '5',
        'placeholder': 'Body'
        } )
    )