from django.contrib import admin
from home.models import TemplateData, TeamPhoto, AmbassadorData
# Register your models here.
admin.site.register(TemplateData)

class AmbassadorAdmin(admin.ModelAdmin):
	list_display = (
		'team_name','team_email',)
	def get_queryset(self, request):
		return AmbassadorData.objects.all()
admin.site.register(AmbassadorData, AmbassadorAdmin)

class TeamPhotoAdmin(admin.ModelAdmin):
	list_display = (
		'team_name',)
	def get_queryset(self, request):
		return TeamPhoto.objects.all()

admin.site.register(TeamPhoto, TeamPhotoAdmin)