from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


app_name ="home"

from home.views import (
	TemplatePage,
	HomePage,
	GeneratePdf,
	ExtraView,
	AmbassadorPage,
	)

urlpatterns = [
	path('template-creator/', 
		TemplatePage.as_view(), 
		name="template-creator"),
	path('', HomePage.as_view(), name="home_page"),
	path('pdf', GeneratePdf.as_view(), name="pdf"),
	# path('ea9f91b2cda019730f2891bd12a7a4d6/', ExtraView.as_view(), name="extra"),
	path('ambassador-program/', AmbassadorPage.as_view(), 
		name="ambassador-program"),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)