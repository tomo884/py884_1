from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login,logout
from .models import ReviewModel
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView
from django.urls import reverse_lazy

#add
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def listview(request):
    object_list=ReviewModel.objects.all()
    paginator = Paginator(object_list, 2)
    page = request.GET.get('page',1) # default値を設定
    page_range = paginator.page_range   #add
    articles = paginator.get_page(page) # page(page)を get_page(page)に変更
    return render(request,'list.html',{
        'page': int(page),
        'page_range':page_range,
        "articles":articles,
        })


def signupview(request):
    if request.method=='POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        try:
            User.objects.create_user(username_data,'',password_data)
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザーは既に登録されています。'})
    else:
        #return render(request,'signup.html',{})
        print(User.objects.all())
    return render(request,'signup.html',{})


def signupview(request):
    if request.method=='POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        try:
            User.objects.create_user(username_data,'',password_data)
        except IntegrityError:
            return render(request,'signup.html',{'error':'このユーザーは既に登録されています。'})
    else:
        #return render(request,'signup.html',{})
        print(User.objects.all())
    return render(request,'signup.html',{})

def loginview(request):
    if request.method=='POST':
        username_data=request.POST['username_data']
        password_data=request.POST['password_data']
        user=authenticate(request,username=username_data,password=password_data)
        if user is not None:
            login(request,user)
            return redirect('list')
        else:
            return redirect('login')
    return render(request,'login.html')

def sampleview(request):
    if request.method=='POST':
        return redirect('login')
    else:
        return render(request,'login.html',{})

@login_required
def detailview(request,pk):
    object=ReviewModel.objects.get(pk=pk)
    return render(request,'detail.html',{'object':object})

class CreateClass(CreateView):
    template_name='create.html'
    model=ReviewModel
    fields=('title','content','author','images','evaluation')
    success_url=reverse_lazy('list')

def logoutview(request):
    logout(request)
    return redirect('login')

def evaluationview(request,pk):
    post=ReviewModel.objects.get(pk=pk)
    author_name=request.user.get_username() + str(request.user.id)
    if author_name in post.useful_review_record:
        return redirect('list')
    else:
        post.useful_review= post.useful_review +1
        post.useful_review_record=post.useful_review_record+author_name
        post.save()
        return redirect('list')

