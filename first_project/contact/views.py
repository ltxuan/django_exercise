from django.shortcuts import render
from django.http import HttpResponse
from .forms import contact_Form
from .models import contactFrom
# Create your views here.
def contact(request):
    cf = contact_Form
    return render(request, 'contact/contact.html', {'cf': cf})

def saveContact(request):
    if request.method == "POST":
        cf = contact_Form(request.POST)
        if cf.is_valid():
            saveCF = contactFrom(usename = cf.cleaned_data['usename'],
                                 email = cf.cleaned_data['email'],
                                 body = cf.cleaned_data['body'])
            saveCF.save()
            return HttpResponse("save success")
        else:
            return HttpResponse("not POST")

    