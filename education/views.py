from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from accounts.permission import role_required
from news.models import *
from .forms import *
from .models import *

# Create your views here.
def main(request):
    news = New.objects.all()[:3]
    courses = Course.objects.all()[:1]
    courses_count = Course.objects.count()
    teachers_count = Teacher.objects.count()
    students_count = Student.objects.count()
    context = {
        'news': news,
        'courses': courses,
        'courses_count': courses_count,
        'teachers_count': teachers_count,
        'students_count': students_count,
    }
    return render(request, 'main.html', context)

def course(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'course/courses.html', context)

@role_required('admin')
def add_course_category(request):
    if request.method == 'POST':
        form = AddCourseCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = AddCourseCategory()
    context = {
        'form': form
    }
    return render(request, 'course/add_course_category.html', context)

@role_required('admin')
def add_course(request):
    if request.method == 'POST':
        form = AddCourse(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
    else:
        form = AddCourse()
    context = {
        'form': form
    }
    return render(request, 'course/add_course.html', context)

def course_detail(request, pk):
    q_course = Course.objects.filter(id=pk).first()
    context = {
        'course': q_course
    }
    return render(request, 'course/course_detail.html', context)


def group(request):
    groups = Group.objects.all()
    context = {
        'groups': groups
    }
    return render(request, 'group/group.html', context)


@role_required('admin')
def add_group(request):
    if request.method == 'POST':
        form = AddGroup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_group_student', group_id=form.instance.id)
    else:
        form = AddGroup()
    context = {
        'form': form
    }
    return render(request, 'group/add_group.html', context)


@role_required('admin')
def add_group_student(request, group_id):
    if request.method == 'POST':
        form = AddGroupStudent(request.POST)
        if form.is_valid():
            chosen_group = Group.objects.get(id=group_id)
            chosen_group.students.add(*form.cleaned_data['students'])
            return redirect('admin_panel')
    else:
        form = AddGroupStudent()
    context = {
        'form': form
    }
    return render(request, 'group/add_group_students.html', context)


@role_required('admin')
def group_edit(request, pk):
    q_group = get_object_or_404(Group, pk=pk)
    print(q_group.students)
    available_students = Student.objects.exclude(
        student_group=q_group
    ).distinct()
    context = {
        'group': q_group,
        'available_students': available_students,
    }
    return render(request, 'group/group_edit.html', context)
