from django import forms

class TemplateForm(forms.Form):
    message = forms.CharField(label='Message:', 
    	max_length=500
    	help_text='How you do #DiversityFIRST within your team.',
    	min_length=0,
    	required=True)
    team_name = forms.CharField(label='Team Name:', 
    	max_length=100,
    	min_length=0,
    	helpt_text='Your team name.'
    	required=True)