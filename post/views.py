from __future__ import unicode_literals
from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404


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