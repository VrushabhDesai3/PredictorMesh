from django.http import request
from django.shortcuts import render, redirect
from Profile.models import Profile
from django.core import serializers
import pickle

def profile(request):
    if request.method == 'POST':

        profile = Profile.objects.all()
        query = profile.filter(user_id=request.user.id)
        profile2 = query.get()

        clgName = request.POST['clgName']
        course = request.POST['course']
        backlogs = int(request.POST['backlogs'])
        ugMarks = request.POST['CGPA']
        ugMarks = float(request.POST['CGPA'])
        examName = request.POST.get('examName', profile2.examName)
        examScore = float(request.POST['examScore'])
        experience = float(request.POST['experience'])
        paperLevel = request.POST.get('paperLevel', profile2.paperLevel)
        user_id = request.user.id
        # is_private = request.POST.get('is_private', False);
        IELTSscore = 0
        PTEscore = 0
        TOEFELscore = 0

        if examName == 'IELTS':
            IELTSscore = examScore
        if examName == 'PTE':
            PTEscore = examScore
        if examName == 'TOEFEL':
            TOEFELscore = examScore

        if paperLevel == 'None':
            paperLevel = 0
        if paperLevel == 'Local':
            paperLevel = 1
        if paperLevel == 'National':
            paperLevel = 2
        if paperLevel == 'International':
            paperLevel = 3

        filename = 'linearModel.sav'
        loaded_model = pickle.load(open(filename, 'rb'))
        result = loaded_model.predict([[IELTSscore, PTEscore, TOEFELscore, backlogs, ugMarks, experience, paperLevel]])
        result = result * 100

        paperLevel = request.POST.get('paperLevel', profile2.paperLevel)# For String Value

        if Profile.objects.filter(user_id=user_id).exists():
            Profile.objects.filter(user_id=user_id).update(clgName=clgName, course=course, backlogs=backlogs, ugMarks=ugMarks, examName=examName, examScore=examScore, experience=experience, paperLevel=paperLevel, isProfile=True, score=result)
        else:
            profile = Profile.objects.create(clgName=clgName, course=course, backlogs=backlogs, ugMarks=ugMarks, examName=examName, examScore=examScore, experience=experience, paperLevel=paperLevel, user_id=user_id, isProfile=True, score=result)
            profile.user_id = request.user.id
            profile.save()

        return redirect('/')
    else:
        if request.user.is_authenticated:
            profile = Profile.objects.all()
            query = profile.filter(user_id=request.user.id)
            userProfile = query.get()
            return render(request, 'profile.html', {'profile': userProfile})
        else:
            return redirect('/accounts/login')