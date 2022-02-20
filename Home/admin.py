from django.contrib import admin
from Colleges.models import College
from Profile.models import Profile
from Course.models import Course

admin.site.register(College)
admin.site.register(Profile)
admin.site.register(Course)