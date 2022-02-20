from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from Colleges.models import College
from Course.models import Course

# Create your views here.
def course(request):
    return render(request, 'courses.html')

def dsb(request):
    courses = Course.objects.all()
    course = Course.objects.get(name="Data Science Bachelors")
    universities = []
    college = College.objects.all()
    for i in college:
        for j in i.courses:
            if j == 'Data Science B':
                universities.append(i)
    return render(request, 'course-single.html', {'courses': courses, 'clg': universities, 'course': course})

def ceb(request):
    courses = Course.objects.all()
    course = Course.objects.all().first()
    universities = []
    college = College.objects.all()
    for i in college:
        for j in i.courses:
            if j == 'Computer Science B':
                universities.append(i)
    return render(request, 'course-single.html', {'courses': courses, 'clg': universities, 'course': course})

def dsm(request):
    courses = Course.objects.all()
    course = Course.objects.get(name="Data Science Masters")
    universities = []
    college = College.objects.all()
    for i in college:
        for j in i.courses:
            if j == 'Data Science M':
                universities.append(i)
    return render(request, 'course-single.html', {'courses': courses, 'clg': universities, 'course': course})

def csm(request):
    courses = Course.objects.all()
    course = Course.objects.get(name="Computer Science Masters")
    universities = []
    college = College.objects.all()
    for i in college:
        for j in i.courses:
            if j == 'Computer Science M':
                universities.append(i)
    return render(request, 'course-single.html', {'courses': courses, 'clg': universities, 'course': course})