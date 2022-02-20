from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from Colleges.models import College
from Contact.models import Contact
from Course.models import Course
from Profile.models import Profile


def home(request):

    colleges = College.objects.order_by("id")[:5]
    universities = College.objects.all().count()
    users = User.objects.all().count()
    course = Course.objects.all().count()
    if request.user.is_authenticated:
        profile = Profile.objects.all()
        query = profile.filter(user_id=request.user.id)
        userProfile = query.get()
        notification = Contact.objects.filter(notification=True).count()

        return render(request, 'index.html', {'colleges': colleges, 'profiles': userProfile, 'users': users, 'uni': universities, 'course': course, 'notification': notification})
    return render(request, 'index.html', {'colleges': colleges, 'users': users, 'uni': universities, 'course': course})
