from django.shortcuts import render,redirect
from .models import Post
from .forms import ImageModelForm
import os

# Create your views here.
def index(request):
    if request.method == 'POST':
        i_form = ImageModelForm(request.POST,request.FILES)
        if i_form.is_valid():
            i_form.save()
            return redirect('/')
    forms = Post.objects.all()
    i_form = ImageModelForm()
    context ={
        'forms':forms,
        'i_form':i_form
    }
    return render(request,'index.html',context)

def deleteBlog(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    else:
        context = {
            'post':post
        }
        return  render(request,'deleteBlog.html',context)


def edit(request,id):
    form = Post.objects.get(id=id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(form.image)> 0:
                os.remove(form.image.path)
            form.image = request.FILES['image']
            form.title = request.POST['title']
            form.content = request.POST['content']
        form.save()
        return redirect('/')
    context = {
        'form':form,
    }
    return render(request,'edit.html',context)
