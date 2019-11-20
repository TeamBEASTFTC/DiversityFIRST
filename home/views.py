import requests


from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from home.template_generator import Badge_Reporter
from django.template.loader import get_template


from django.utils.decorators import method_decorator
from home.forms import TemplateForm, AmbassadorForm
from home.utils import render_to_pdf #created in step 4
from home.models import TeamPhoto

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
			info = form_info.save()

			print('post accepted 2.')
			msg = form_info.cleaned_data['message']
			team_name = form_info.cleaned_data['team_name']
			size = form_info.cleaned_data['size']
			print (msg)
			#print the message out too
			context = {
				"message": msg,
				"team_name": team_name,
				}

			pdf = render_to_pdf(request, 'pdf/poster.html', context, size=size)
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
		template_form = TemplateForm()
		#collecting all the photios and puytting them in a list
		ph_list = []
		ph_data = TeamPhoto.objects.all()
		for photo in ph_data:
			ph_list.append(photo)

		#getting image
		#img_list = []
		#for image in ph_list:
		#	img_list.append(image.Image)

		#list 

		args = {'form': template_form, 'photo_data': ph_list}
		return render(request, self.template_name, args)

	def post(self, request):
		form = TemplateForm()		
		args = {'form': form}

		form_info = TemplateForm(request.POST)
		if form_info.is_valid():
			team_name = form_info.cleaned_data['team_name']
			print (team_name)
			info = form_info.save(commit=False)

			if team_name == '' or team_name == None:
				team_name == 'N/A'
			info.team_name = team_name
			info.save()

			msg = form_info.cleaned_data['message']
			print('post accepted.')
			size= form_info.cleaned_data['size']
			#print the message out too
			context = {
				"message": msg,
				"team_name": team_name,
				}

			pdf = render_to_pdf(request, 'pdf/poster.html', context, size=size)
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

class ExtraView(TemplateView):
	template_name = 'home/extra.html'

class AmbassadorPage(TemplateView):
	template_name = "home/ambassador-program.html"

	def get(self, request):
		form = AmbassadorForm()
		args = {'form': form}
		return render(request, self.template_name, args)


	def post(self, request):
		form = AmbassadorForm()
		args = {'form': form}

		form_info = AmbassadorForm(request.POST)

		if form_info.is_valid():
			print('AmbassadorForm form accepted')
			team_name = form_info.cleaned_data['team_name']
			team_email = form_info.cleaned_data['team_email']
			message = form_info.cleaned_data['message']
			info = form_info.save(commit=False)

			if message == '' or message == None:
				message = 'Undecided'
			info.message = message
			info.save()

			print('AmbassadorForm saved')
			args['form_saved'] = True
			query_data= {
			'team_name': team_name,
			'team_email': team_email,
			'message': message,
			}

			r = requests.post('https://hooks.zapier.com/hooks/catch/2174411/o4xkken/', data=query_data)

		return render(request, self.template_name, args)
