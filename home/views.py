from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from home.template_generator import Badge_Reporter
from django.template.loader import get_template


from django.utils.decorators import method_decorator
from home.forms import TemplateForm
from home.utils import render_to_pdf #created in step 4

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
			context = {
				"message": msg,
				"team_name": team_name,

				}

			pdf = render_to_pdf(request, 'pdf/poster.html', context)
			if pdf:
				
				response =  HttpResponse(pdf, content_type='application/pdf')
				filename = "diversityFIRST"
				content = "inline; filename='%s'" %(filename)
				download = request.GET.get("download")
				if download:
					content = "attachment; filename='%s'" %(filename)
				response['Content-Disposition'] = content
				return response
			return HttpResponse("Not Found")

		else:
			print(False)
			return render(request, self.template_name, args)

class HomePage(TemplateView):
	template_name = 'home/home_page.html'

	def get(self, request):
		return render(request, self.template_name)


class PosterView(PDFTemplateView):
	template_name = 'hello.html'

class GeneratePdf(View):
	def get(self, request, *args, **kwargs):
		context = {
				"invoice_id": 123,
				"customer_name": "Felix Hall",
				"amount": 1399.99,
				"date": "Today",
			}

		pdf = render_to_pdf('pdf/invoice.html', context)
		if pdf:
			response =  HttpResponse(pdf, content_type='application/pdf')
			filename = "filename"
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not Found")