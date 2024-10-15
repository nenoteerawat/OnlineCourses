from django.shortcuts import redirect, render
from .forms import CourseForm
from .models import Courses

def courseFormView(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'courseapp/course.html'
    context = {'form': form}
    return render(request, template_name, context)

def showView(request):
    obj = Courses.objects.all()
    template_name = 'courseapp/show.html'
    context = {'obj': obj}
    return render(request, template_name, context)

def updateView(request, f_oid):
    obj = Courses.objects.get(oid=f_oid)
    form = CourseForm(instance=obj)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'courseapp/course.html'
    context = {'form': form}
    return render(request, template_name, context)

def deleteView(request, f_oid):
    obj = Courses.objects.get(oid=f_oid)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    template_name = 'courseapp/confirmation.html'
    context = {'obj': obj}
    return render(request, template_name, context)
