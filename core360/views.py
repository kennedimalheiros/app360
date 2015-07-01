from django.shortcuts import render
from core360.models import Office, Department, Employee, Quiz, Evaluation, Options, Question
from django.shortcuts import render, redirect, get_object_or_404
from core360.forms import DepartmentForm
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    data = {}
    data['evaluation_list'] = Evaluation.objects.filter(person_will_answer_form__user=request.user)
    return render(request, 'core360/dashboard.html', data)

@login_required
def department_list(request):
    data = {}
    data['department_list'] = Department.objects.all()
    return render(request, 'core360/department_list.html', data)

@login_required
def department_create(request, template_name='core360/department_form.html'):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_avaliacoes_department')
    return render(request, template_name, {'form':form})

@login_required
def department_update(request, pk, template_name='core360/department_form.html'):
    department = get_object_or_404(Department, pk=pk)
    form = DepartmentForm(request.POST or None, instance=department)
    if form.is_valid():
        form.save()
        return redirect('url_avaliacoes_department')
    return render(request, template_name, {'form':form, 'department':department})

@login_required
def department_delete(request, pk, template_name='core360/confirm_delete.html'):
    department = get_object_or_404(Department, pk=pk)    
    if request.method=='POST':
        department.delete()
        return redirect('url_avaliacoes_department')
    return render(request, template_name, {'object':department})

@login_required
def evaluation (request):
    data = {}
    data['evaluation_list'] = Evaluation.objects.filter(person_will_answer_form__user=request.user)
    return render(request, 'core360/evaluation.html', data)