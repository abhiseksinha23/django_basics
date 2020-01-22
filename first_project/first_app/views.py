from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord,Topic,Webpage
# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_record':webpage_list}
    #my_dict = {'insert_me':" learning "}
    #return render(request, 'first_app/index.html', context=my_dict)
    return render(request, 'first_app/index.html', context=date_dict)
