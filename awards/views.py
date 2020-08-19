from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project
from .forms import NewProjectForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    projects = Project.get_projects()
    return render(request, 'awards/index.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request,'new_project.html',{"form":form})    
