from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Academy, Department, NoteUpload, Subject

def academy(request):
    academyList = Academy.objects.all()
    return render(
        request,
        'Academy/allAcademy.html',
        context={
            "academyList_dict": academyList,
        }
    )

def computerDepartment(request):
    academyList = Academy.objects.all()
    departmentList = Department.objects.all()
    departmentListDict = {}
    for a in academyList:
        if (a.academy == "資訊電機學院"):
            dList = [d.department for d in Department.objects.filter(academy=a)]
            departmentListDict[a.academy] = dList

    return render(
        request,
        'Department/computer.html',
        context={
            "comDepartmentList_dict": departmentListDict,
        }
    )

def businessDepartment(request):
    academyList = Academy.objects.all()
    departmentList = Department.objects.all()
    departmentListDict = {}
    for a in academyList:
        if (a.academy == "商學院"):
            dList = [d.department for d in Department.objects.filter(academy=a)]
            departmentListDict[a.academy] = dList

    return render(
        request,
        'Department/business.html',
        context={
            "busDepartmentList_dict": departmentListDict,
        }
    )

def CSsubject(request):
    departmentList = Department.objects.all()
    subjectListDict = {}
    for d in departmentList:
        if (d.department == "資訊工程學系"):
            sList = [s.subject for s in Subject.objects.filter(department=d)]
            subjectListDict[d.department] = sList
    return render(
        request,
        'Subject/subject.html',
        context={
            "subjectList_dict": subjectListDict,
        }
    )

def Calculas(request):
    academyList = Academy.objects.all()
    departmentList = Department.objects.all()
    subjectList = Subject.objects.all()
    noteList = NoteUpload.objects.all()
    noteListDict = {}
    for a in academyList:
        if a.academy == "資訊電機學院":
            for d in departmentList:
                if d.department == "資訊工程學系":
                    for s in subjectList:
                        if s.subject == "微積分":
                            nList = [n.images for n in NoteUpload.objects.filter(subject=s)]
                            noteListDict[s.subject] = nList
                            print(NoteUpload.objects.filter(subject=s))

    print(noteListDict)
    return render(
        request,
        'Notes/note.html',
        context={
            "noteList_dict": noteListDict,
        }
    )