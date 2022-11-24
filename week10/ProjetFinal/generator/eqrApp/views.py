from django.shortcuts import redirect, render
import json
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from eqrApp import models, forms
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required



def context_data():
    context = {
        'page_name' : '',
        'page_title' : 'Generator',
        'system_name' : 'Generator',
        'topbar' : True,
        'footer' : True,
    }

    return context


""" 
def login_page(request):
    context = context_data()
    context['topbar'] = False
    context['footer'] = False
    context['page_name'] = 'login'
    context['page_title'] = 'Login'
    return render(request, 'login.html', context)"""

"""def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')"""


def homee(request):
    context = context_data()
    context['page'] = 'home'
    context['page_title'] = 'Home'
    context['employees'] = models.Employee.objects.count()
    return render(request, 'home.html', context)

"""def logout_user(request):
    logout(request)
    return redirect('login-page')"""



def employee_list(request):
    context =context_data()
    context['page'] = 'employee_list'
    context['page_title'] = 'Employee List'
    context['employees'] = models.Employee.objects.all()

    return render(request, 'employee_list.html', context)


def manage_employee(request, pk=None):
    context =context_data()
    if pk is None:
        context['page'] = 'ajout_employee'
        context['page_title'] = 'Ajouter Nouveau Employee'
        context['employee'] = {}
    else:
        context['page'] = 'edit_employee'
        context['page_title'] = 'Modifier Employee'
        context['employee'] = models.Employee.objects.get(id=pk)

    return render(request, 'manage_employee.html', context)


def save_employee(request):
    resp = { 'status' : 'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = "Pas de donner."

    else:
        if request.POST['id'] == '':
            form = forms.SaveEmployee(request.POST, request.FILES)
        else:
            employee = models.Employee.objects.get(id = request.POST['id'])
            form = forms.SaveEmployee(request.POST, request.FILES, instance = employee)
        if form.is_valid():
            form.save()
            if request.POST['id'] == '':
                messages.success(request, f"{request.POST['first_name']} a ete ajoute avec succes.")
            else:
                messages.success(request, f"{request.POST['first_name']} a ete modifie avec succes.")
            resp['status'] = 'success'
        else:
            for field in form:
                for error in field.errors:
                    if not resp['msg'] == '':
                        resp['msg'] += str("<br />")
                    resp['msg'] += str(f"[{field.label}] {error}")

    return HttpResponse(json.dumps(resp), content_type="application/json")


def view_card(request, pk =None):
    if pk is None:
        return HttpResponse("Employee ID Invalid")
    else:
        context = context_data()
        context['employee'] = models.Employee.objects.get(id=pk)
        return render(request, 'view_id.html', context)


#def view_scanner(request):
    #context = context_data()
    #return render(request, 'scanner.html', context)



def view_details(request, code = None):
    if code is None:
        return HttpResponse("Employee code  Invalid")
    else:
        context = context_data()
        context['employee'] = models.Employee.objects.get(employee_code=code)
        return render(request, 'view_details.html', context)


def delete_employee(request, pk=None):
    resp = { 'status' : 'failed', 'msg' : '' }
    if pk is None:
        resp['msg'] = "Pas de donner"
    else:
        try:
            models.Employee.objects.get(id=pk).delete()
            resp['status'] = 'success'
            messages.success(request, 'Employee a ete supprimer avec succes')
        except:
            resp['msg'] = "eureur de suppression"

    return HttpResponse(json.dumps(resp), content_type="application/json")
