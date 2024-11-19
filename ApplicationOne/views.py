from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view

from ApplicationOne.forms import StudentForm
from ApplicationOne.models import Student, Course
from ApplicationOne.serializers import StudentSerializer, CourseSerializer


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    data = Student.objects.all()
    return render(request, 'About.html',{'data':data})


def contact(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = StudentForm()
        return render(request, 'contact.html', {'form': form})





def edit(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your changes have been saved Successfully!')
            return redirect('About')
        else:
            messages.error(request, 'Please check form details')
    else:
        form = StudentForm(instance=student)
    return render(request, 'edit.html',{'form':form, 'student':student})

def delete(request, id):
    student = get_object_or_404(Student, id=id)
    try:
        student.delete()
        messages.success(request, 'Student has been deleted Successfully!')
        return redirect('About')
    except Exception as e:
        messages.error(request, 'Student not deleted')

    return redirect('About')

@api_view(['GET','POST'])
def studentApi(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def courseApi(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)