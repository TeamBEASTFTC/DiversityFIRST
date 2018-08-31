from django import forms

class TemplateForm(forms.Form):
    message = forms.CharField(label='Message:', 
    	max_length=500,
    	min_length=5,
    	required=True)
    team_name = forms.CharField(label='Team Name:', 
    	max_length=100,
    	min_length=5,
    	required=True)