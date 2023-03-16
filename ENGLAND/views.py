from django.shortcuts import render

# Create your views here.
def England(request):
    E={'name':'kohli'}
    return render(request,'Team.html',context=E)