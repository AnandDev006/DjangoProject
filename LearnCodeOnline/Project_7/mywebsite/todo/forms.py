from django import forms

class todoForm(forms.Form):
    text = forms.CharField( max_length = 50,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Django TODO',
            } )
        )