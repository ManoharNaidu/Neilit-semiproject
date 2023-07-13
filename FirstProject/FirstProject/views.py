from django.http import HttpResponse
from django.shortcuts import render,redirect

age = 50

def home(request):
    Marks = {
        'Social':50,
        'Hindi':60,
        'English':70,
        'Maths':80,
    }
    per = sum(Marks.values())/4
    hobbies = ['Batminton','Cricket']
    data = {
        'Name':'Manu',
        'Address':'Andhra',
        'age':age,
        'Sem':'7th sem',
        'College':'NIELIT',
        'Marks':Marks,
        'Percentage': per,
        'Hobbies':hobbies,
    }

    # if request.method == "POST":
    #     name = request.POST['Name']
    #     num = int(request.POST['Age'])
    #     user = {
    #         'username':name,
    #         'age':num
    #     }
    #     return render(request,'index2.html',user)
    # else:
    return render(request,'Home.html',data)

def contacts(request):
    return render(request,'Contacts.html')

def about(request):
    data = {'age':age}
    return render(request,'About.html',data) 

def services(request):
    return render(request,'Services.html')

def login(request):
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        psd1 = request.POST['password1']
        psd2 = request.POST['password2']

        if psd1 == psd2:
            user = {'username':name,
                    'email':email}
            return render(request,'loggedin.html',user)
    return render(request,'login.html')