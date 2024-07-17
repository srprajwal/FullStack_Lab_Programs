from django.shortcuts import render, redirect
from .models import Course
from .forms import StudentForm, CourseForm

def index(request):
  courses = Course.objects.all()
  return render(request, 'index.html', {'courses': courses})

def register_student(request):
  if request.method == 'POST':
    form = StudentForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = StudentForm()
  return render(request, 'register_student.html', {'form': form})

def register_course(request):
  if request.method == 'POST':
    form = CourseForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = CourseForm()
  return render(request, 'register_course.html', {'form': form})

def student_list(request, course_id):
  course = Course.objects.get(id=course_id)
  students = course.students.all()
  return render(request, 'student_list.html', {'students': students, 'course': course})