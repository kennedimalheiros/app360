from django.shortcuts import render
from core360.models import Office, Department, Employee, Quiz, Evaluation, Options, Question, Answer
from django.shortcuts import render, redirect, get_object_or_404
from core360.forms import DepartmentForm, FormAnswer, FormQuestion
from django.contrib.auth.decorators import login_required
#from core360.report import write_to_pdf

@login_required
def dashboard(request):
    data = {}
    evaluations = Answer.objects.filter(
        evaluation__person_will_answer_form__user = request.user, answer__isnull=True).distinct('evaluation')
    data['evaluations'] = evaluations  
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

#@login_required
#def evaluation (request):
#   data = {}
#    data['evaluation_list'] = Evaluation.objects.filter(person_will_answer_form__user=request.user)
#    return render(request, 'core360/evaluation.html', data)

@login_required
def answers_respond(request, pk_answer):
    data = {}
    answer = get_object_or_404(Answer, pk=pk_answer)
    form = FormAnswer(request.POST or None, instance=answer)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return evaluation_respond(request, answer.evaluation.id)

    data['form'] = form
    return render(request, 'core360/answer_respond.html', data)


@login_required
def evaluation_respond(request, pk_evaluation):
    data = {}
    evaluation = get_object_or_404(Evaluation, pk=pk_evaluation)
    answers = Answer.objects.filter(evaluation__person_will_answer_form__user = request.user,
        evaluation = evaluation, answer__isnull=True)
    if answers:
#        data['form'] = FormRating(instance=evaluation)
        data['answers'] = answers
        return render(request, 'core360/answers_pending_list.html', data)
    else:
        return redirect('url_avaliacoes_home')

@login_required
def question_respond(request, pk_question, pk_evaluation):
    data = {}
     
    evaluation = get_object_or_404(Evaluation, pk=pk_evaluation)
    question = get_object_or_404(Question, pk=pk_question)

    if request.method != 'POST':
        form = FormQuestion(instance=question)

        data['form'] = form

        return render(request, 'core360/question_respond_form.html', data)
    else:
        form = FormQuestion(request.POST or None, instance=question)

        if form.is_valid():
            question = form.save(commit=False)
            answer = Answer(
                evaluation_id=pk_evaluation,
                question_id=pk_question,
                answer=form)
            return redirect('url_question_respond')
        else:
            data['form'] = form
            return render(request, 'core360/question_respond_form.html', data)



@login_required
def reports(request):
    data = {}
    answers = Answer.objects.filter(
       evaluation__employee_assessed__user = request.user, answer__isnull=False)
#    import pdb; pdb.set_trace()
    data['answers'] = answers
    return render(request, 'core360/report.html', data)

@login_required
def reports_boss(request):
    data = {}
    answers = Answer.objects.filter(
       evaluation__employee_assessed__boss__user = request.user, answer__isnull=False)
#    import pdb; pdb.set_trace()
    data['answers'] = answers
    return render(request, 'core360/reports_boss.html', data)


@login_required
def listar_clientes_cadastrados(request):
    clientes = Cliente.objects.all()
    return write_to_pdf('relatorio.html', {'clientes': clientes}, 'nome_do_arquivo_pdf')