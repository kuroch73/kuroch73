from django.shortcuts import render

# Create your views here.
def index(request) :
    return render(request, template_name='index/index.html')
def output(request):
    myName = request.GET.get('myName')
    return render(request, template_name='index/output.html',context={'myName': myName})
