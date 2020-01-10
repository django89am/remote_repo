from django.shortcuts import render
from .models import StudentData
from .forms import StudentDataForm
from django.http.response import HttpResponse
from django.views import generic

def makeentry(request):
    if request.method == "GET":
        sform = StudentDataForm()
        return render(request,'student_form.html',{'sform':sform})
    else:
        sform = StudentDataForm(request.POST)
        if sform.is_valid():
            sname = request.POST.get('student_name')
            cname = request.POST.get('course_name')
            cfee = request.POST.get('course_fee')
            iname = request.POST.get('institute_name')
            qual = request.POST.get('qualification')
            loc = request.POST.get('location_name')

            data = StudentData(
                student_name=sname,
                course_name=cname,
                course_fee=cfee,
                institute_name=iname,
                qualification=qual,
                location_name=loc
            )
            data.save()
            sform = StudentDataForm()
            return render(request,'student_form.html',{'sform':sform})
        else:
            return HttpResponse("Data Missed")


class IndexView(generic.ListView):
    context_object_name = 'list'
    template_name = 'student_index.html'
    def get_queryset(self):
        return StudentData.objects.all()

class DetailsView(generic.DetailView):
    model = StudentData
    template_name = 'stduent_details.html'