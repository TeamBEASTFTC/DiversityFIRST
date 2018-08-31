from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404

from home.template_generator import Badge_Reporter


from django.utils.decorators import method_decorator
from home.forms import TemplateForm

from easy_pdf.views import PDFTemplateView


class TemplatePage(TemplateView):
	template_name = 'home/template-creator.html'

	def get(self, request):
		template_form = TemplateForm()
		args = {'form': template_form}
		return render(request, self.template_name, args)
	def post(self, request):
		form = TemplateForm()		
		args = {'form': form}

		form_info = TemplateForm(request.POST)
		if form_info.is_valid():
			print(True)
			msg = request.POST.get('message', '')
			team_name = request.POST.get('team_name', '')
			#print the message out too
			return Badge_Reporter.Badge_Report(self, request, message=msg, name=team_name)
		else:
			print(False)
			return render(request, self.template_name, args)


class HomePage(TemplateView):
	template_name = 'home/home_page.html'

	def get(self, request):
		return render(request, self.template_name)


class PosterView(PDFTemplateView):
    template_name = 'hello.html'