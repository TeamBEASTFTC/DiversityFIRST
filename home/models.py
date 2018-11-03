from django.db import models

# Create your models here.

class TemplateData(models.Model):



	message = models.CharField(
		max_length=500,
#		min_length=5,
#		required=False
)

	team_name = models.CharField(max_length=50, 
#		required=False
		)
	size = models.CharField(max_length=3, 
#		required=False
		)

	def __str__(self):
		return self.team_name

class TeamPhoto(models.Model):
	team_name = models.CharField(max_length=50, 
#		required=False
		)
	Image = models.ImageField(upload_to='team_image', blank=False)