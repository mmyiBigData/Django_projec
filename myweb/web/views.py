#coding=utf-8
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post,Element,Fire,Air,Earth,Water,Sname
from .forms import PostForm
from django.contrib.auth.models import User
from django.db import connection
from django.views.decorators.csrf import csrf_exempt


me = User.objects.get(username='mmyi16')
post_form=PostForm()

# Create your views here.
def index(request):
	fire = Fire.objects.all()
	air = Air.objects.all()
	earth = Earth.objects.all()
	water = Water.objects.all()
	flist=[]
	for ff in fire:
		ffire = ff.ename
		flist.append(ffire)
	alist =[]
	for aa in air:
		aair = aa.ename
		alist.append(aair)
	wlist =[]
	for ww in water:
		wwater = ww.ename
		wlist.append(wwater)
	elist =[]
	for ee in earth:
		eearth = ee.ename
		elist.append(eearth)
		
	try:
		sfire = request.GET['sfire']
		# searth = request.GET['searth']
		# sair = request.GET['sair']
		# swater = request.GET['swater']
		
		if sfire in flist:
			outfire = Sname.objects.filter(ename=sfire)
			print outfire.name
			print 'ok'
		elif sfire in elist:
			outfire = Sname.objects.filter(ename=sfire)
		elif sfire in alist:
			outfire = Sname.objects.filter(ename=sfire)
		elif sfire in wlist:
			outfire = Sname.objects.filter(ename=sfire)
		else:
			outfire=None
			print 'none'
			pass
			
	except:
		pass
	
	return render(request, 'web/index.html',locals())

def forms(request):
	posts=Post.objects.filter(create_date__lte=timezone.now())\
						.order_by('-id')[:10]
	return render(request, 'web/forms.html',{'posts':posts,'post_form':post_form})
	
@csrf_exempt	
def add_record(request):
	if request.POST:
		title = request.POST['title'].encode('utf-8')
		text = request.POST['text'].encode('utf-8')
		newpost = Post.objects.create(author=me,title=title,text=text)
	return redirect('/web/forms')

def list(request,id):
	posts = Post.objects.filter(id__gte=id)[:2]
	if len(posts) == 1:
		post = posts[0]
		next_post = post
	else:
		post = posts[0]
		next_post = posts[1]
	return render(request, 'web/list.html',locals())