
#pdf generations

#uncomment this if needed
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

#returns a pdf report of all badges within the right time range
class Badge_Reporter():
	def Badge_Report(self, request, message, name):
		# Create the HttpResponse object with the appropriate PDF headers.
		response = HttpResponse(content_type='application/pdf')
		response['Content-Disposition'] = 'attachment; filename="diversityFIRSTposter.pdf"'

		buffer = BytesIO()

		# Create the PDF object, using the BytesIO object as its "file."
		p = canvas.Canvas(buffer)

		# Draw things on the PDF. Here's where the PDF generation happens.
		# See the ReportLab documentation for the full list of functionality.


		p.drawString(100, 750, "We put #DiversityFIRST by...")
		
		p.showPage()
		p.save()

		# Get the value of the BytesIO buffer and write it to the response.
		pdf = buffer.getvalue()
		buffer.close()
		response.write(pdf)
		return response

'''
		x_cor = 100
		y_cor = 720

		for badge in pioneer_list:
			scout = User.objects.get(username=badge.scout_username)
			p.drawString(x_cor, y_cor, "%s (%s %s)"%(badge.Pioneer_Badge, scout.first_name, scout.last_name))
			y_cor -= 25

		'''

'''
		#Explorer Badge listing
		p.drawString(100, 750, "Explorer Badges:")
		x_cor = 100
		y_cor = 720

		for badge in explorer_list:
			scout = User.objects.get(username=badge.scout_username)
			p.drawString(x_cor, y_cor, "%s (%s %s)"%(badge.Explorer_Badge, scout.first_name, scout.last_name))
			y_cor -= 25
		p.showPage()

		#Adventurer Badge listing
		p.drawString(100, 750, "Adventurer Badges:")
		x_cor = 100
		y_cor = 720

		for badge in adventurer_list:
			scout = User.objects.get(username=badge.scout_username)
			p.drawString(x_cor, y_cor, "%s (%s %s)"%(badge.Adventurer_Badge, scout.first_name, scout.last_name))
			y_cor -= 25
		
		p.showPage()

		#Other Badge listing
		p.drawString(100, 750, "Other Badges:")
		x_cor = 100
		y_cor = 720

		for badge in other_list:
			scout = User.objects.get(username=badge.scout_username)
			p.drawString(x_cor, y_cor, "%s%s (%s %s)"%(badge.Proficiency_Badge, badge.Other_Badge, scout.first_name, scout.last_name))
			y_cor -= 25
		'''
		# Close the PDF object cleanly.
		