from django import forms

class TemplateForm(forms.Form):
    message = forms.CharField(label='Message:', 
    	max_length=500,
    	help_text='How you do #DiversityFIRST within your team.',
    	min_length=5,
    	required=False)
    team_name = forms.CharField(label='Team Name:', 
    	max_length=100,
    	min_length=5,
    	help_text='Your team name.',
    	required=False)