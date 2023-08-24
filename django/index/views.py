import random

from django.shortcuts import render

# Create your views here.
def indexView(request):
    return render(request,"index.html")

def passwordView(request):
    newpassword = "123456"
    lenght = int(request.GET.get('lenght'))
    text = list('abcdefghijgklmnopqrstuvwxyz')
    if request.GET.get('upper'):
        text.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for i in range(lenght):
        newpassword += text[random.randint(0,len(text)-1)]
    return render(request,'password.html', {'newpassword':newpassword})
