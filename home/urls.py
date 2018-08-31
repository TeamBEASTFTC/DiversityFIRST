from django.contrib import admin
from django.urls import path, include


app_name ="home"

from home.views import (
	TemplatePage,
	HomePage,
	)

urlpatterns = [
	path('template-creator/', 
		TemplatePage.as_view(), 
		name="template-creator"),
	path('', HomePage.as_view(), name="home_page"),

]
