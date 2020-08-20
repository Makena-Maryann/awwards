from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Project,Profile
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

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'awards/search.html',{"message":message,"projects":searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'awards/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    projects = Project.objects.filter(user=current_user).all()
    profile = Profile.objects.filter(user=current_user)
    return render(request, 'awards/profile.html', {'projects':projects,'profile':profile})
