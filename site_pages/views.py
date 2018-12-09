from django.shortcuts import render
#from django_tables2 import RequestConfig
#from .models import Client, Product
#from .tables import ClientTable, ProductTable

def main(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def statistics(request):
    return render(request, 'statistics.html')
    
def statistics1(request, template_name='statistics.html', **kwargs):
    'Example view that inserts content into the dash context passed to the dash application'

    context = {}

    # create some context to send over to Dash:
    dash_context = request.session.get("django_plotly_dash", dict())
    dash_context['django_to_dash_context'] = "I am Dash receiving context from Django"
    request.session['django_plotly_dash'] = dash_context

    return render(request, template_name=template_name, context=context)
