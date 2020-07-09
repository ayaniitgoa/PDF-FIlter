from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import Files
import PyPDF2
# Create your views here.


def home(request):
    context = {}
    return render(request, 'main/upload.html', context)


def upload(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files')

    form = FileForm()
    context = {'form': form}
    return render(request, 'main/upload.html', context)


def is_valid_query_param(param):
    return param != '' and param is not None


def files(request):
    files = Files.objects.all().distinct()

    name = request.POST.get('name')
    branch = request.POST.get('branch')
    skill = request.POST.get('skill')
    if is_valid_query_param(name):
        files = files.filter(name__icontains=name)
    if is_valid_query_param(branch):
        files = files.filter(branch__icontains=branch)
    # print(skill)
    allfiles = []
    if is_valid_query_param(skill):
        for cv in files:
            pdf = cv.pdf
            pdfRead = PyPDF2.PdfFileReader(pdf)
            ok = False
            for i in range(pdfRead.getNumPages()):
                page = pdfRead.getPage(i)
                pagecontent = page.extractText()

                if skill in pagecontent:
                    ok = True
                    allfiles.append(pdf)
                    break
        files = files.filter(pdf__in=allfiles)
    context = {'files': files}
    return render(request, 'main/files.html', context)
