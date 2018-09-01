from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


app_name ="home"

from home.views import (
	TemplatePage,
	HomePage,
	GeneratePdf,
	)

urlpatterns = [
	path('template-creator/', 
		TemplatePage.as_view(), 
		name="template-creator"),
	path('', HomePage.as_view(), name="home_page"),
	path('pdf', GeneratePdf.as_view(), name="pdf"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
