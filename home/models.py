from django.db import models


# Create your models here.
class AmbassadorData(models.Model):
	team_name = models.CharField(max_length=50, blank=False
#		required=False
	)
	team_email = models.EmailField(max_length=200, blank=False)

	message = models.CharField(max_length=1000, blank=True)


	def __str__(self):
		return '%s'% (self.team_name)

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
	Image = models.ImageField()


	def __str__(self):
		return '%s'% (self.team_name)