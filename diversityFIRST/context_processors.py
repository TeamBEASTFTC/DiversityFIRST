from django.conf import settings # import the settings file

def google_tag(request):
	#return value as a dictionary
	return {'GOOGLE_ANALYTICS_TAG': settings.GOOGLE_ANALYTICS_TAG}