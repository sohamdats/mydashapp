from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    return render(request,'index.html')




def full_list(request):
    data = models.Timestamp.objects()
    return render(request,'full_list.html',{'data':data})


def detail_page(request,ts):
    data = models.Timestamp.objects(time=ts)
    return render(request,'detail_page.html',{'data':data})

def usage_detail_page(request,ts,name,usage=None):
    data = models.Timestamp.objects(time=ts)
    return render(request,'usage_detail_page.html',{'data':data,'name':name,'usage':usage})

