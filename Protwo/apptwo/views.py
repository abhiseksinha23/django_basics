from django.shortcuts import render
from apptwo.forms import NewUserForm
from django.http import HttpResponse
from apptwo.models import User
# Create your views here.

def index(request):
    #return HttpResponse("HELLO")
    return render(request, 'apptwo/index.html',)
#def help(request):
#    d = {'insert_me':'Help Page'}
#    return render(request, 'apptwo/index.html', context=d)

def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user_record':user_list}
    return render(request, 'apptwo/user.html', context =user_dict)
    # form = NewUserForm()
    #
    # if request.method == "POST":
    #     form = NewUserForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save(commit=True)
    #         return index(request)
    #     else:
    #         print("ERROR")
    #
    # return render(request, 'apptwo/user.html',{'form': form})
