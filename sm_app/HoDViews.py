from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from sm_app.models import CustomUser


def admin_home(request):
    return render(request, 'sm_app/hod_template/home_content.html')


def add_teacher(request):
    return render(request, 'sm_app/hod_template/add_teacher_template.html')

def add_staff_save(requst):
    if requst.method != 'POST':
        return HttpResponse('Method is not allowed!')
    else:
        first_name = requst.POST.get('first_name')
        last_name = requst.POST.get('last_name')
        username = requst.POST.get('username')
        email = requst.POST.get('email')
        password = requst.POST.get('password')
        address = requst.POST.get('address')

        try:
            user = CustomUser.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                             last_name=last_name, user_type=2)
            user.teacher.address = address
            user.save()
            messages.success(requst, 'Successfully Added Teacher.')
            return HttpResponseRedirect('/add_teacher')
        except:
            messages.error(requst, 'Failed to add teacher.')
            return HttpResponseRedirect('/add_teacher')
