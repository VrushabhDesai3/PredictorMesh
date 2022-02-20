from django.http import request
from django.shortcuts import render

# Create your views here.
from Profile.models import Profile


def about(request):
    if request.user.is_authenticated:
        profile = Profile.objects.all()
        query = profile.filter(user_id=request.user.id)
        userProfile = query.get()
        return render(request, 'about.html', {'profiles': userProfile})
    return render(request, 'about.html')