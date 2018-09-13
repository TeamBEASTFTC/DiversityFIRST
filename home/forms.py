from django import forms
from home.models import TemplateData


class TemplateForm(forms.ModelForm):

	class Meta:
		Size_choices = (
			('A4', 'A4'),
			('A3', 'A3'),
			)
		model = TemplateData
		fields = ('message','team_name', 'size') 

		widgets = {
		'message': forms.TextInput(attrs={'id': "message_field"}),
		'size': forms.Select(choices=Size_choices),
		}
		labels = {
		'message': 'Your Message:',
		'team_name': 'Team Name:',
		'size': 'Poster Size:'
		}

		help_text = {
		'message': 'How you do #DiversityFIRST within your team.', 
		'team_name': 'Your team name.',
		}

	def __init__(self, *args, **kwargs):
		super(TemplateForm, self).__init__(*args, **kwargs)
		msg = self.fields['message']
		msg.min_length = 5
		msg.required = False


		t_m = self.fields['team_name']
		t_m.required = True

		sz = self.fields['size']
		sz.required = False
