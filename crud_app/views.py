from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from .forms import StudentRegistration
from .models import User


# Create your views here.
"""
This function for add and show the data on same page.
"""
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    print("----!@#$%^&*()--")
    return render (request, 'addandshow.html', {'form':fm, 'stu':stud})

"""
Update student data.
get the requested data and id, 
if the method is Get return the requested Id data. else update the data into sqlite Database.

Input parameters: request and Id.
output parameters: Save the data into the database. sqlite
"""
def update_data(request, id):
    if request.method == 'POST':
        print("-------=============-----------")
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            print("###############################################################")
            fm.save()

    else:
        print("Method is get ===================")
        pi = User.objects.get(pk=id)
        print(f"di: {id} and pi {pi}")
        fm = StudentRegistration(instance=pi)
        # print(f"fm new data : {fm}")
    return render(request, 'updatestud.html', {'form':fm})
 

"""
This Functionsis detele the record if requested ID. and redirect to the same page.
"""
def delete_data(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return HttpResponseRedirect('/')


