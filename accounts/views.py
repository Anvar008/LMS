from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .permission import role_required


# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main')
    else:
        form = SignUpForm()

    context = {
        'form': form
    }
    return render(request, 'authentication/sign_up.html', context)

def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('main')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'authentication/sign_in.html', context)

@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    return redirect('sign_in')

@role_required('admin')
def add_user(request):
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            if form.cleaned_data['role'] == 'teacher':
                Teacher.objects.create(user=user)
            elif form.cleaned_data['role'] == 'student':
                Student.objects.create(user=user)
            return redirect('admin_panel')
    else:
        form = NewUser()
    context = {
        'form': form
    }
    return render(request, 'user/new_user.html', context)

@role_required('admin')
def admin_panel(request):
    return render(request, 'admin_panel.html')

@login_required(login_url='sign_in')
@role_required('teacher')
def teacher_profile(request):
    teacher = Teacher.objects.filter(user=request.user.id).first()
    if request.method == 'POST':
        form = TeacherProfile(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_profile')
    else:
        form = TeacherProfile(instance=teacher)
    context = {
        'form': form,
        'teacher': teacher
    }
    return render(request, 'user/teacher_profile.html', context)

@login_required(login_url='sign_in')
@role_required('student')
def student_profile(request):
    student = Student.objects.filter(user=request.user.id).first()
    if request.method == 'POST':
        form = StudentProfile(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_profile')
    else:
        form = StudentProfile(instance=student)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'user/student_profile.html', context)
