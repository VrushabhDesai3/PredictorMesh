from django.http import request
from django.shortcuts import render

# Create your views here.
from Contact.models import Contact
from Profile.models import Profile


def contact(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
            name = request.POST['name']
            email = request.POST['email']
            message = request.POST['message']
            phone = request.POST['phone']
            contact = Contact.objects.create(name= name, email= email, message= message, phone= phone)
            contact.save()
            return render(request, 'contact.html')
        return render(request, 'contact.html')
    else:
        if request.user.is_authenticated:
            profile = Profile.objects.all()
            query = profile.filter(user_id=request.user.id)
            userProfile = query.get()
            return render(request, 'contact.html',{'profiles': userProfile})
        return render(request, 'contact.html')