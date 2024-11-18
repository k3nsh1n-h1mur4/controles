import pathlib
import sqlite3
import bcrypt
from PIL import Image
import pandas as pd
from openpyxl import Workbook
from .connection import Connection

from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.views import LoginView, LogoutView

import control.views
from .forms import RegistrationForm, loginForm, ValidateMatriculaForm, ValidateTelefonoForm, EstructuraEdicionForm
from .models import User

# Create your views here.
def index(request):
    return HttpResponse('Index')

def register(request):
    title = 'Registro'
    error = None
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            is_staff = form.cleaned_data['is_staff']
            is_active = form.cleaned_data['is_active']
            is_superuser = form.cleaned_data['is_superuser']
            print(username, password, is_staff, is_active, is_superuser)
            user = User.objects.create_user(username=username, password=password, email=email, is_staff=is_staff, is_active=is_active, is_superuser=is_superuser)

            if user:
                print(user)
        return redirect('index')
                #login(request)
                
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form, 'title': title, 'error': error})

def login(request):
    title = 'Login'
    error = None
    form = AuthenticationForm()

    """
    form = loginForm(request.POST or None)
    if request.method == 'POST':
        user = User.objects.get(username=request.POST['username'])
        print(user)
        if user.check_password(request.POST['password']):
            request.session['_auth_user_id'] = user.id
            return redirect('register')
        else:
            return HttpResponse('Invalid username or password')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            login(request)
    """

    return render(request, 'login.html', {'form': form, 'title': title, 'error': error})


@login_required
def user_logout(request):
    print(request.session.keys())
    print(request.session.get('_auth_user_id'))
    print(request.session.values())
    if request.method == 'POST':
        request.session.pop('_auth_user_id', '')
        request.session.pop('_auth_user_hash', '')
        request.session.clear()
        request.session['_auth_user_id'] = None
        logout(request)
    return render(request, 'registration/logged_out.html', {'title': 'Logged Out'})
    

def upload_handle_img(img, name):
    with Image.open(img) as img:
        print(img)
        img.save(os.path.join(settings.UPLOAD_FILES, name))
        
        
def getLastId():
    cnx = Connection.getConnection()
    cur = cnx.cursor()
    cur.execute("SELECT id FROM estructuratbl order by id desc limit 1;")
    rowid = cur.fetchone()
    cnx.commit()
    print(rowid)
    if not rowid[0]:
        return
    else: return rowid[0] + 1


@login_required
def ValidateMatricula(request):
    title = 'Validar Matricula'
    error = ''
    ctx = None
    #form = ValidateMatriculaForm()
    if request.method == 'POST':
        form = ValidateMatriculaForm(request.POST)
        matricula = request.POST['matricula']
        cnx = Connection.getConnection()
        cur = cnx.cursor()
        cur.execute("SELECT matricula FROM estructuratbl WHERE matricula={0}".format(matricula))
        ctx = cur.fetchone()
        cnx.commit()
        cur.close()
        if ctx:
            error = 'Matricula ya registrada'
        else:
            return redirect('validate_telefono')
    else:
        form = ValidateMatriculaForm()

        return render(request, 'index.html', {'title' : title, 'error' : error, 'ctx' : ctx, 'form' : form})
    return render(request, 'index.html', {'title' : title, 'error' : error, 'ctx' : ctx, 'form' : form})
    
@login_required
def ValidateTelefono(request):
    title = 'Validar Teléfono'
    error = ''
    ctx = None
    #form = ValidateMatriculaForm()
    if request.method == 'POST':
        form = ValidateTelefonoForm(request.POST)
        num_cel = request.POST['num_cel']
        cnx = Connection.getConnection()
        cur = cnx.cursor()
        cur.execute("SELECT num_cel FROM estructuratbl WHERE num_cel={0}".format(num_cel))
        ctx = cur.fetchone()
        cnx.commit()
        cur.close()
        if ctx:
            error = 'Teléfono ya registrado'
            return redirect('validate_matricula')
        else:
            return redirect('new_register')
    else:
        form = ValidateTelefonoForm()

        return render(request, 'validaTel.html', {'title' : title, 'error' : error, 'ctx' : ctx, 'form' : form})
    return render(request, 'validaTel.html', {'title' : title, 'error' : error, 'ctx' : ctx, 'form' : form})
 
@login_required    
def new_register(request):
    title = 'Nuevo Registro'
    error = None
    form = EstructuraRegistrationForm()
    if request.method == 'POST':
        form = EstructuraRegistrationForm(request.POST, request.FILES)
        matricula = request.POST['matricula']
        nombre = request.POST['nombre']
        ftrab = request.FILES['ftrab']
        ffirma = request.FILES['ffirma']
        fnac = request.POST['fnac']
        categoria= request.POST['categoria']
        adsc_act= request.POST['adsc_act']
        adsc_ant= request.POST['adsc_ant']
        turno= request.POST['turno']
        domicilio= request.POST['domicilio']
        colonia= request.POST['colonia']
        municipio= request.POST['municipio']
        seccional= request.POST['seccional']
        num_cel= request.POST['num_cel']
        email = request.POST['email']
        Resp_100 = request.POST['Resp_100']
        Resp_10= request.POST['Resp_10']
        part_trab= request.POST['part_trab']
        inf_adic= request.POST['inf_adic']
        descansos= request.POST['descansos']
        vac_prog= request.POST['vac_prog']
        servicio= request.POST['servicio']
        promocion= request.POST['promocion']
        movilizacion= request.POST['movilizacion']
        asis_reu = request.POST['asis_reu']
        voto_25Sept = request.POST['voto_25Sept']
        engrupo = request.POST['engrupo']
        status = request.POST['status']
        inf_admin = request.POST['inf_admin']
        mi_resp = request.POST['mi_resp']
        upload_handle_img(ftrab, ftrab.name)
        folder = os.path.join(settings.BASE_DIR, 'images')
        imgPersonPath = os.path.join(folder, ftrab.name)
        
        upload_handle_img(ffirma, ffirma.name)
        imgSignPath = os.path.join(folder, ffirma.name)
        data = [
            (getLastId(),matricula,nombre.upper(),imgPersonPath,imgSignPath,fnac,categoria,adsc_act,adsc_ant,turno,domicilio.upper(),colonia.upper(),municipio.upper(),seccional,num_cel,email,Resp_100.upper(),Resp_10.upper(),part_trab.upper(),inf_adic.upper(),descansos.upper(),vac_prog.upper(),servicio.upper(),promocion.upper(),movilizacion.upper(),asis_reu.upper(),voto_25Sept.upper(),engrupo.upper(),status.upper(),inf_admin.upper(),mi_resp.upper(),request.user.id),
        ]
        cnx = Connection.getConnection()
        cur = cnx.cursor()
        
        cur.executemany("INSERT INTO estructuratbl VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);", data)
        cnx.commit()
        cur.close()
        return JsonResponse({"data" : "Registro Realizado"})
        
        
    return render(request, 'new_register.html', {'form': form, 'title': title})    
    
@login_required    
def list(request):
    title = 'Listado General'
    error = None
    if request.method == 'GET':
        cnx = Connection.getConnection()
        cur = cnx.cursor()
        cur.execute("SELECT * FROM estructuratbl WHERE userId_id = {0}".format(request.user.id) )
        ctx = cur.fetchall()
        cnx.commit()
        total = len(ctx)
        paginator = Paginator(ctx, 15)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        cur.close()
        cnx.close()
    return render(request, 'list.html', {'title': title, 'error': error, 'page_obj' : page_obj, 'total': total})



@login_required
def details(request, id):
    if not request.user.is_authenticated:
        return redirect(f"{settings.LOGIN_URL}?next{request.path}")
    id = id
    title = 'Detalles del Registro'
    error = None
    cnx = Connection.getConnection()
    cur = cnx.cursor()
    cur.execute('SELECT * FROM estructuratbl WHERE id = {0};'.format(id))
    ctx = cur.fetchone()
    if not ctx:
        error = 'No hay Registros por Mostrar'
    cnx.commit()
    cur.close()
    #print(type(ctx[3]))
    #p = pathlib.PureWindowsPath(ctx[3])
    #rep = ctx[3].replace('\\', '/')
    #print(rep)
    #with Image.open(rep) as picture:
    #    picture.show()
    return render(request, 'details.html', {'title': title, 'error': error, 'ctx': ctx, 'rep' : ctx[3]})


@login_required
def delete(request,id):
    id = id
    cnx = Connection.getConnection()
    cur = cnx.cursor()
    cur.execute("DELETE FROM estructuratbl WHERE id = {0}".format(id))
    cnx.commit()
    cur.close()
    return redirect('list')

def ExportE(result, user):
    wb = Workbook()
    ws = wb.active
    for i in result:
        ws.append(i)
    wb.save('Datos' + user + '.xlsx')
    


@login_required
def export_excel(request):
    title = 'Exportar a Excel'
    error = None
    if request.method == 'GET':
        cnx = Connection.getConnection()
        cur = cnx.cursor()
        cur.execute("SELECT * FROM estructuratbl WHERE userId_id = {0}".format(request.user.id))
        ctx = cur.fetchall()
        cnx.commit()
        cur.close()
        ExportE(ctx, request.user.username)
        if ctx == None:
            return
        else:
            createdFile = glob.iglob(os.path.join(BASE_DIR, '*.xlsx'), recursive=True)
            last_file = max(createdFile, key=os.path.getctime)
            response = FileResponse(open(last_file, 'rb'), as_attachment=True)
            return response
        

@login_required
def viewImage(request, slug):
    slug = slug
    return HttpResponse(slug)


@login_required
def edit(request, id):
    title = 'Editar Registro'
    id = id
    cnx = Connection.getConnection()
    cur = cnx.cursor()
    cur.execute("SELECT * FROM estructuratbl WHERE id=?;", [id,])
    ctx = cur.fetchone()
    cnx.commit() 
    form = EstructuraEdicionForm()
    if request.method == 'POST':
        form = EstructuraEdicionForm(request.POST, initial=ctx)
        print(form)
    return render(request, 'editar.html', {'title':title, 'ctx':ctx, 'form':form})


@login_required
def save_edit(request, id):
    id = id
    title = 'Guardar Edicion'
    if request.method == 'POST':
        matricula = request.POST['matricula']
        nombre = request.POST['nombre']
        ftrab = request.POST['ftrab']
        ffirma = request.POST['ffirma']
        fnac = request.POST['fnac']
        categoria= request.POST['categoria']
        adsc_act= request.POST['adsc_act']
        adsc_ant= request.POST['adsc_ant']
        turno= request.POST['turno']
        domicilio= request.POST['domicilio']
        colonia= request.POST['colonia']
        municipio= request.POST['municipio']
        seccional= request.POST['seccional']
        num_cel= request.POST['num_cel']
        email = request.POST['email']
        Resp_100 = request.POST['Resp_100']
        Resp_10= request.POST['Resp_10']
        part_trab= request.POST['part_trab']
        inf_adic= request.POST['inf_adic']
        descansos= request.POST['descansos']
        vac_prog= request.POST['vac_prog']
        servicio= request.POST['servicio']
        promocion= request.POST['promocion']
        movilizacion= request.POST['movilizacion']
        asis_reu = request.POST['asis_reu']
        voto_25Sept = request.POST['voto_25Sept']
        engrupo = request.POST['engrupo']
        status = request.POST['status']
        inf_admin = request.POST['inf_admin']
        mi_resp = request.POST['mi_resp'] 
        #upload_handle_img(ftrab, ftrab.name)
        #folder = os.path.join(settings.BASE_DIR, 'images')
        #imgPersonPath = os.path.join(folder, ftrab.name)
        
        #upload_handle_img(ffirma, ffirma.name)
        #imgSignPath = os.path.join(folder, ffirma.name)
        """
        
        data = [
            (matricula,nombre.upper(),imgPersonPath,imgSignPath,fnac,categoria,adsc_act,adsc_ant,turno,domicilio.upper(),colonia.upper(),municipio.upper(),seccional,num_cel,email,Resp_100.upper(),Resp_10.upper(),part_trab.upper(),inf_adic.upper(),descansos.upper(),vac_prog.upper(),servicio.upper(),promocion.upper(),movilizacion.upper(),asis_reu.upper(),voto_25Sept.upper(),engrupo.upper(),status.upper(),inf_admin.upper(),mi_resp.upper(),request.user.id),
        ]
        """
        cnx = Connection.getConnection()
        cur = cnx.cursor()
        
        cur.execute("UPDATE estructuratbl SET matricula=?,nombre=?,ftrab=?,ffirma=?,fnac=?,categoria=?,adsc_act=?,adsc_ant=?,turno=?,domicilio=?,colonia=?,municipio=?,seccional=?,num_cel=?,email=?,Resp_100=?,Resp_10=?,part_trab=?,inf_adic=?,descansos=?,vac_prog=?,servicio=?,promocion=?,movilizacion=?,asis_reu=?,voto_25Sept=?,engrupo=?,status=?,inf_admin=?,mi_resp=?,user_id_id_id=? WHERE id=?;", (matricula,nombre.upper(),ftrab,ffirma,fnac,categoria,adsc_act,adsc_ant.upper(),turno,domicilio.upper(),colonia.upper(),municipio.upper(),seccional,num_cel,email,Resp_100.upper(),Resp_10.upper(),part_trab.upper(),inf_adic.upper(),descansos.upper(),vac_prog.upper(),servicio.upper(),promocion.upper(),movilizacion.upper(),asis_reu.upper(),voto_25Sept.upper(),engrupo.upper(),status.upper(),inf_admin.upper(),mi_resp.upper(),request.user.id, id))
        cnx.commit()
        cur.close()
        return redirect('list')
        #return JsonResponse({"data" : "Registro Realizado"})
        
    return HttpResponse('Registro Editado Correctamente')    
    #return render(request, 'new_register.html', {'title': title})          
