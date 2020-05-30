from django import forms

class GeeksForm(forms.Form):

	name = forms.CharField()
	event = forms.CharField()
	image = forms.FileField()
	amount = forms.CharField()
