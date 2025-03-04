from django.shortcuts import render,redirect
from .models import Blog
from .forms import BlogForm

# Create your views here.

def home(request):
    blogs = Blog.objects.all()

    context={
        'blogs':blogs
    }

    return render(request,'index.html',context)


def edit(request,pk ):
    blogs = Blog.objects.get(pk=pk)
    
    if request.method =="POST":
        model_form=BlogForm(request.POST,request.FILES,instance=blogs)
        if model_form.is_valid():
            model_form.save()
            return redirect('home')
    else:
        model_form=BlogForm(instance=blogs)

    context={
        'model_form':model_form
    }

    return render(request,'edit.html',context)


def delete(request ,pk):
    blogs = Blog.objects.get(pk=pk)
    blogs.delete()
    return redirect('home')


def add_item(request):

    model_form=BlogForm()
    if request.method =="POST":
        model_form=BlogForm(request.POST,request.FILES)
        if model_form.is_valid():
            model_form.save()
            return redirect('home')
    else:
        model_form=BlogForm()

    context={
        'model_form':model_form
    }

    return render(request,'edit.html',context)



def view_item(request ,pk):
    
    blogs = Blog.objects.filter(pk=pk)
    context={
        'blogs':blogs
    }

    return render(request,'view_item.html',context)

    