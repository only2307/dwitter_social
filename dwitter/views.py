from django.shortcuts import render, redirect
from .models import Profile, Dweet
from .forms import DweetForm
from django.contrib.auth.decorators import login_required
# from django.contrib import messages

# Create your views here.
@login_required
def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")
    
    followed_dweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")
    return render(request, "dwitter/dashboard.html", {"form": form, "dweets": followed_dweets})

def profile_list(request):
    #  get all user profiles except for your own, which you accomplish with .exclude().
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "dwitter/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    
    profile = Profile.objects.get(pk=pk)
    # processing form
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "dwitter/profile.html", {"profile": profile})
        