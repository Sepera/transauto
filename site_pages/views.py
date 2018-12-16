from django.shortcuts import render
#from django_tables2 import RequestConfig
#from .models import Client, Product
#from .tables import ClientTable, ProductTable
from django.http import HttpResponse
import smtplib

def main(request):
    return render(request, 'index.html')

def contact(request):
    if 'name' in request.GET:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        name = request.GET['name']
        email = request.GET['email']
        phone = request.GET['phone']
        if 'message' in request.GET:
            message = request.GET['message']
        else: message = ''

        msg = "\r\n".join([
            "From: kravchenkos.spb@gmail.com",
            "To: annamyakshina1@gmail.com",
            "Subject: Just a message",
            "Заявка",
            "Имя: %s"%name,
            "Телефон: %s"%phone,
            "email: %s"%email,
            "Комментарий: %s"% message

        ]).encode('utf-8')
        fromaddr = "kravchenkos.spb@gmail.com"
        toaddrs = "annamyakshina1@gmail.com"
        username = 'kravchenkos.spb@gmail.com'
        password = 'quantphys2016'

        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
    return render(request, template_name= 'contact.html')

def about(request):
    return render(request, template_name= 'about.html')

def calculator(request):
    return render(request, template_name= 'calculator.html')

def notfound(request):
    return render(request, template_name= '404.html')


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
