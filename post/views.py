from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.contrib import messages



def post_detail(request, post_id):
    obj = get_object_or_404(Post , id = post_id)
    context = {
        "instance": obj,
    }
    return render(request, 'post_detail.html',context)

def post_list(request):
    details = Post.objects.all()
    context3 = {
        "list": details,
    }
    return render(request, 'post_list.html',context3)
def post_create(request):
    form = PostForm(request.POST or None)
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
    form = PostForm(request.POST or None ,instance=obj)
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
