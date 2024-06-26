from django.shortcuts import render
from django.http import HttpResponse
from nadhapp.models import *

def index(request):
  return render(request,'base.html')



def about(request):
  return render(request,'About.html')


def faq(request):
  tit=FAQ.objects.all()
  return render(request,'FAQ.html',{'i':tit})




