from django.contrib import admin
from home.models import TemplateData, TeamPhoto
# Register your models here.
admin.site.register(TemplateData)

class TeamPhotoAdmin(admin.ModelAdmin):
	list_display = (
		'team_name',)
	def get_queryset(self, request):
		return TeamPhoto.objects.all()

admin.site.register(TeamPhoto, TeamPhotoAdmin)