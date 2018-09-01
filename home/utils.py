from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template, render_to_string

from xhtml2pdf import pisa
from django.conf import settings


'''
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None
'''
from weasyprint import HTML, CSS
def render_to_pdf(request, template_src, context_dict={}):
	html_string = render_to_string(template_src, context_dict)
#	template = get_template(template_src)
#	html = template.render(context_dict)
	pdf = HTML(
		string=html_string,
		base_url=request.build_absolute_uri()
		).write_pdf(
		stylesheets=[CSS(settings.STATIC_ROOT +  '/base/poster.css')],
		presentational_hints=True)
	return pdf