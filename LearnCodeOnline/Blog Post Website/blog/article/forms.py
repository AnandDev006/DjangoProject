from django import forms

class BlogForm(forms.Form):
	articleName = forms.CharField( max_length = 20,
		widget = forms.TextInput( attrs = {
				'id' : 'InputName',
				'class' : 'form-control',
				'placeholder' : 'Title'
			}
		)
	)

	articleBody = forms.CharField(
		widget = forms.Textarea( {
			'class' : 'form-control',
			'id' : 'comment',
			'rows' : '5',
			'placeholder' : 'Body'
			}
		)
	)