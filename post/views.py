from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Post , Event
from django.shortcuts import get_object_or_404
from .forms import PostForm , UserSignUp ,UserLogin ,EventForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404 ,JsonResponse
from django.utils import timezone 
from django.db.models import Q
from django.contrib.auth import authenticate , login ,logout
from datetime import date





def search_bar(request):
    obj = Card.all()
    details = []
    for x in obj:
        details = details + [x.names]
    context = {
    "details": details,
    }
    return JsonResponse(context,safe=False)

def userlogin(request):
    context={}
    form = UserLogin()
    context['form'] = form 
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user= authenticate(username=username,password=password)
            if auth_user is not None:
                login(request,auth_user)
                return redirect("post:home")

            messages.warning(request,"wrong user name or password")
            return redirect("post:login")
        messages.warning(request,form.errors)
        return redirect("post:login")
    return render(request, 'login.html',context)


def usersignup(request):
    context={}
    form = UserSignUp()
    context['form'] = form 
    if request.method == "POST":
        form = UserSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            password = user.password
            user.set_password(password)
            user.save()
            auth_user= authenticate(username=username,password=password)
            login(request,auth_user)
            return redirect("post:home")
        messages.error(request,form.errors)
        return redirect("post:signup")
    return render(request, 'signup.html',context)

def userlogout(request):
    logout(request)
    return redirect("post:home")


def post_home(request):
    obj = Post.objects.all().first()
    if Event.objects.all().exists():
        today = timezone.now().date()
        event = Event.objects.all()
        x = False
        for y in event:
            if y.startdate_event >= today:
                event = y
                x = True 
                break

        context = {
        "x": x,
        "today": today,
        "user": request.user,
        "last_event": event,
        "post_last": obj,
        }
    else:
        context = {
        "user": request.user,
        "post_last": obj,
        }
    return render(request, 'post_home.html', context)
def post_detail(request, slug):
    obj = get_object_or_404(Post , slug=slug)
    today = timezone.now().date()
    if obj.publish > today or obj.draft:
        if not(request.user.is_superuser or request.user.is_staff):
            raise Http404
    context = {
        "instance": obj,
        "user": request.user,
    }
    return render(request, 'post_detail.html',context)

def post_list(request):
    today = timezone.now().date()
    if request.user.is_superuser or request.user.is_staff :
        details = Post.objects.all()
    else:
        details = Post.objects.filter(draft=False).filter(publish__lte=today)
    
    query = request.GET.get("q")
    if query:
        details= details.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(author__first_name__icontains=query) | 
            Q(author__last_name__icontains=query)
            ).distinct()
    paginator = Paginator(details, 4) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context3 = {
        "user": request.user,
        "list": contacts,
        "today": today,
    }
    return render(request, 'post_list.html',context3)
def post_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit= False)
        obj.author = request.user 
        obj.save()
        messages.success(request,"your post has been created")
        return redirect ("post:list")
    context = {
    "form": form,
    "user": request.user
    }
    return render(request, 'post_create.html',context)
    return render(request, 'post_create.html',context)
def post_update(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None ,request.FILES or None , instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"the post has been updated")
        return redirect("post:list")
    context = {
        "form": form,
        "obj": obj,
        "user": request.user,
    }
    return render(request, 'post_update.html', context)

def post_delete(request, slug):
    post_obj = Post.objects.get(slug=slug)
    post_obj.delete()
    messages.warning(request, "the post has been deleted")
    return redirect("post:list")

def event_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
        raise Http404
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("post:eventlist")
    context = {
    "form": form,
    "user": request.user,
    }
    return render(request,'event_create.html',context)
def event_list(request):
    details = Event.objects.all()
    paginator = Paginator(details, 4) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    context3 = {
        "list": contacts,
        "user": request.user,
    }
    return render(request, 'event_list.html',context3)

def event_delete(request, event_slug):
    post_obj = Event.objects.get(event_slug=event_slug)
    post_obj.delete()
    messages.warning(request, "the post has been deleted")
    return redirect("post:eventlist")
def event_update(request, event_slug):
    obj = get_object_or_404(Event, event_slug=event_slug)
    form = EventForm(request.POST or None ,request.FILES or None , instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"the post has been updated")
        return redirect("post:eventlist")
    context = {
    "user": request.user,
    "form": form,
    "obj": obj,
    }
    return render(request, 'event_update.html', context)