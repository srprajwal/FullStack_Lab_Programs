from django.shortcuts import render

def disp(request):
  res ={'fruits':['apple','mango','orange'],
        'student':['stu1','stu2','stu3']}
  return render(request,'prg.html',res)

