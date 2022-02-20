from django.contrib.postgres.search import SearchVector
from django.http import request, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Colleges.models import College
from Profile.models import Profile
from PredictorMesh import helpers

def Colleges(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            search = request.POST['search']
            queryset = College.objects.filter(name__icontains=search)
            queryset = helpers.pg_records(request, queryset, 6)
            if not queryset:
                return HttpResponse("No match Found!")
            else:
                return render(request, 'colleges.html', {'colleges': queryset})
        return redirect('/accounts/login')

    if request.user.is_authenticated:
        profile = Profile.objects.all()
        query = profile.filter(user_id=request.user.id)
        userProfile = query.get()
        if userProfile.isProfile == 1:
            Colleges = College.objects.order_by("id")
            Colleges = helpers.pg_records(request, Colleges, 6)
            return render(request, 'colleges.html', {'colleges': Colleges, 'profiles': userProfile})
        else:
            return render(request, 'profile.html', {'profile': userProfile})
    return redirect('/accounts/login')

def recColleges(request):
    if request.user.is_authenticated:
        profile = Profile.objects.all()
        query = profile.filter(user_id=request.user.id)
        userProfile = query.get()
        if userProfile.isProfile == 1:
            Score = userProfile.score
            Colleges = College.objects.filter(cutOff__lte=Score).order_by('rank')
            Colleges = helpers.pg_records(request, Colleges, 6)
            return render(request, 'colleges.html', {'colleges': Colleges, 'profiles': userProfile})
        else:
            return render(request, 'profile.html', {'profile': userProfile})
    return redirect('/accounts/login')