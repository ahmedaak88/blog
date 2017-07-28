from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Post ,Event
from django.shortcuts import get_object_or_404
from .forms import PostForm ,EventForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from urllib.parse import quote


def post_home(request):
    obj = Post.objects.all().first()
    event = Event.objects.all().first()
    context = {
    "last_event": event,
    "post_last": obj,
    }
    return render(request, 'post_home.html', context)
def post_detail(request, post_id):
    obj = get_object_or_404(Post , id = post_id)
    context = {
        "instance": obj,
        "share_string": quote(obj.content),
    }
    return render(request, 'post_detail.html',context)

def post_list(request):
    details = Post.objects.all()
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
    }
    return render(request, 'post_list.html',context3)
def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request,"your post has been saved")
        return redirect("post:list")

    context = {
    "form": form,
    }
    return render(request, 'post_create.html',context)
def post_update(request, post_id):
    obj = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None ,request.FILES or None , instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"the post has been updated")
        return redirect("post:list")
    context = {
    "form": form,
    "obj": obj,
    }
    return render(request, 'post_update.html', context)

def post_delete(request, post_id):
    post_obj = Post.objects.get(id=post_id)
    post_obj.delete()
    messages.warning(request, "the post has been deleted")
    return redirect("post:list")

def event_create(request):
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {
    "form": form,
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
    }
    return render(request, 'event_list.html',context3)

def event_delete(request, post_id):
    post_obj = Event.objects.get(id=post_id)
    post_obj.delete()
    messages.warning(request, "the post has been deleted")
    return redirect("post:eventlist")
def event_update(request, post_id):
    obj = get_object_or_404(Event, id=post_id)
    form = EventForm(request.POST or None ,request.FILES or None , instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request,"the post has been updated")
        return redirect("post:eventlist")
    context = {
    "form": form,
    "obj": obj,
    }
    return render(request, 'event_update.html', context)