import http
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required,user_passes_test,permission_required
from .models import *
from django.http import HttpResponse, JsonResponse
from . import forms
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import requests
from datetime import date
from bs4 import BeautifulSoup as ny_bs


base_api = 'https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&'
# Create your views here.
def home(request):
    jumlah_user = User.objects.all().count()
    if request.GET.get('nama') and request.GET.get('tanggal_lahir'):
        nama = request.GET.get('nama')
        tanggal_lahir = request.GET.get('tanggal_lahir')
        url_zodiak = f'{base_api}nama={nama}&tanggal={tanggal_lahir}'
        req_ramalan = requests.get(url_zodiak)
        data_ramalan = req_ramalan.json()
        api_data_ramalan = data_ramalan['data']
        nama_zodiak = data_ramalan['data']['zodiak']

        # GET DATA RAMALAN DARI WEB LAIN
        bs_zodiak_url = requests.get(f'http://gemintang.com/ramalan-bintang-setiap-hari/ramalan-{nama_zodiak}-hari-ini/').text
        bs_soup = ny_bs(bs_zodiak_url,'html.parser')
        for bs_zodiak in bs_soup.find_all('td',{'align':'center','colspan':'2'})[1:2]:

            ramalan = bs_zodiak.text.replace('(adsbygoogle = window.adsbygoogle || []).push({});','').replace('''\n''','').replace('. ','''.\n''')
            
        ramalan_zodiak = ramalan 
        context = {'api_data_ramalan':api_data_ramalan,'ramalan_zodiak':ramalan_zodiak,'jumlah_user':jumlah_user}
    else:
        context = {'jumlah_user':jumlah_user}
    return render(request, 'frontend/home.html', context)

def kritikSaran(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        pesan = request.POST.get('pesan')

        KritikSaran.objects.create(
            nama = nama,
            email = email,
            pesan = pesan,
        )
        messages.success(request, 'Pesanmu Telah Terkirim, Terima Kasih Telah Membantu Kami.')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.warning(request, 'Pesanmu Gagal Terkirim, Silakan Coba Dalam Beberapa Menit Lagi.')
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request,'frontend/home.html')

def komentar(request):
    if request.method == 'POST':
        Komentar.objects.create(
            user = request.user,
            zodiak = request.POST.get('zodiak'),
            ramalan = request.POST.get('ramalan'),
            komentar = request.POST.get('komentar'),
        )
        messages.success(request, 'Komentar Telah Terkirim, Terima Kasih')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.warning(request, 'Komentar Gagal Terkirim, Silakan Coba Dalam Beberapa Menit Lagi.')
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request,'frontend/home.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'operator/dashboard.html')

def loginPage(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    if username and password:
        if request.method == 'POST':

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect(request.META.get('HTTP_REFERER'))
            else:
                messages.info(request, 'Username OR password is incorrect')
                return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect('home')
    return render(request, 'frontend/home.html')

def logout_view(request):
    logout(request)
    return redirect('home')

# EDIT PROFIl
@login_required(login_url='home')
def profil(request):
    user = request.user
    form = forms.UserForm(instance=user)

    if request.method == 'POST':
        form = forms.UserForm(request.POST, instance=user)
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')
        if request.POST.get('password1'):
            if request.POST.get('password1') == request.POST.get('password2'):
                user.set_password(request.POST.get('password1'))
            else:
                 messages.error(request, "Password & Konfirmasi Password Harus Sama.", extra_tags="danger" )
                 return redirect('profil')
        user.save()
        messages.success(request, "Sukses Mengubah Profil." )
        return redirect('profil')

    context = {'user':user,'form':form}
    return render(request, 'operator/profil.html', context)