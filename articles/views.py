from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
 
def index(request):

	return HttpResponse("You are at index.page")

def special_case_2003(request):
	
	return HttpResponse("You are at speical articel page in 2003 year")



def year_archive(request, year):

	return render(request, 'articles/archive.html', context={'year':year})



def month_archive(request, year, month):
	
	return render(request, 'articles/archive.html', context={'year':year,'month':month})



def article_detail(request, year, month, day):
	
	return render(request, 'articles/archive.html',context={'year':year,'month':month,'day':day})