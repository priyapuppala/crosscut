from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
from investor.models import Investor, InvestorProfile


def home(request):
    return render(request, 'ehome.html')


def logout(request):
    del request.session['name']
    del request.session['email']
    return redirect('/home/')


def idea(request, mail):
    if request.method == 'POST':
        form = EntreprenuerIdeasForm(request.POST, request.FILES)
        if form.is_valid():
            form1 = form.save(commit=False)
            email = request.session['email']
            form1.fullname = Entreprenuer.objects.values_list('fullname', flat=True).get(email=email)
            form1.invmail = mail
            form1.email = email
            form1.location = Entreprenuer.objects.values_list('location', flat=True).get(email=email)
            form1.mobileno = Entreprenuer.objects.values_list('mobileno', flat=True).get(email=email)
            form1.save()
            return render(request, 'esuccessful.html')
    else:
        form = EntreprenuerIdeasForm
    return render(request, 'eideas.html', {'form': form})


# start-up content approve or delete after deletion render details
def details(request, mail):
    inv = InvestorProfile.objects.get(email=mail)  # select * from investors
    return render(request, 'edetails.html', {'mail': mail, 'inv': inv})


def services(request):  # normal page
    return render(request, 'eservices.html')


def about(request):  # normal page
    return render(request, 'eabout.html')


def successful(request):  # continue to requests page form
    return render(request, 'esuccessful.html')


def registerlogin(request):
    if request.method == 'POST':
        if request.POST.get('submit') == 'login':
            form = EntreprenuerLoginForm(request.POST)
            if form.is_valid():
                mail = form.data["email"]
                pwd = form.data["password"]
                if mail == 'admin@gmail.com' and pwd == 'crosscut':
                    return redirect('/crosscutadmin/home')
                flag = Entreprenuer.objects.filter(Q(email__iexact=mail) & Q(password__iexact=pwd))
                if flag:
                    request.session['email'] = mail
                    enp = Entreprenuer.objects.values_list('fullname', flat=True).get(email=mail)
                    request.session['name'] = enp
                    return redirect('/entreprenuer/home')
                else:
                    form = EntreprenuerForm
                    return render(request, 'elogin.html', {'form': form})
        elif request.POST.get('submit') == 'register':
            form = EntreprenuerForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/entreprenuer/login')
    else:
        form = EntreprenuerForm
    return render(request, 'elogin.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = EntreprenuerContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/entreprenuer/home')
    else:
        form = EntreprenuerContactForm
    return render(request, 'econtact.html', {'form': form})


def content(request):
    email = request.session["email"]
    investors = Investor.objects.all()  # select * from investors
    return render(request, 'econtent.html', {'investors': investors, 'email': email})
