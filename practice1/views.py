from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
	foo = "Welcome to index page"
	return render(request, 'practice1/index.html', context={'foo':'Boo'})


# def index(request):
# 	t = loader.get_template('practice1/index.html')
# 	c = {'foo':'boo'}
# 	return HttpResponse(t.render(c,request))