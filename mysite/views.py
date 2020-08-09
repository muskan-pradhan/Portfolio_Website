from django.shortcuts import render
import requests,json
from .models import Contact
def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        r = requests.get('https://type.fit/api/quotes')
        json_data = json.loads(r.text)
        res = [sub['text'] for sub in json_data]
        res1 = [sub['author'] for sub in json_data]
        quote=str(res[97])+' -'+str(res1[97])
        context = {'quote': quote}
        return render(request, 'mysite/index.html',context)
    else:
        return render(request, 'mysite/index.html')

def portfolio(request):
    return render(request,'mysite/portfolio.html')

def contact(request):
    if request.method == 'POST':
       email_r = request.POST.get('email')
       subject_r = request.POST.get('subject')
       message_r = request.POST.get('message')
       c = Contact(email=email_r,subject=subject_r,message=message_r)
       c.save()

       return render(request, 'mysite/thank.html')
    else:
       return render(request,'mysite/contact.html')
# Create your views here.
