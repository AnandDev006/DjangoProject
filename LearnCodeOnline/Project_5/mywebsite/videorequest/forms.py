from django import forms

class VideoForm(forms.Form):
	videoName = forms.CharField( max_length = 20,
		widget = forms.TextInput( attrs = {
				'id' : 'inputName',
				'class' : 'form-control',
				'placeholder' : 'Name'
			}
		)
	)

	videoDesc = forms.CharField(
		widget = forms.Textarea( {
			'class' : 'form-control',
			'rows' : '5',
			'id' : 'comment',
			'placeholder' : 'Comment'
			}
		)
	)