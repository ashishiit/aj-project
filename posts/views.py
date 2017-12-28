from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Post
from posts.forms import PostForm
from django.contrib import messages
# Create your views here.
def posts_create(request):
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
#         return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form':form,
        }
    return render(request, 'post_form.html', context)

def posts_detail(request,id_num):
    instance = get_object_or_404(Post, id = id_num)
    context = {
        'title':instance.title,
        'instance':instance}
    return render(request, 'posts_detail.html', context)

def posts_list(request):
    queryset = Post.objects.all()
    context = {'queryset':queryset,
               'title': 'List'
               }
    return render(request, 'index.html',context)

def posts_update(request,id_num):
    instance = get_object_or_404(Post, id=id_num)
    form = PostForm(request.POST, instance = instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
#         return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form':form}
    return render(request, 'post_form.html', context)

def posts_delete(request, id_num):
    instance = get_object_or_404(Post, id=id_num)
    instance.delete()
    messages.success(request, 'successfully deleted')
    return redirect('posts:list')

def posts_home(request):
    context = {
        'title':'fuck',
        }
    return render(request,'index.html',context)