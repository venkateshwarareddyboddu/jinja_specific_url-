from django.shortcuts import render

# Create your views here.
def india(request):
    D={'name':'Dhoni'}
    return render(request,'Team.html',context=D)