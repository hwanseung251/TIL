from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, StockForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from contentfetch.models import UserinterestStock
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('contentfetch:stock_finder')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('contentfetch:stock_finder')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('contentfetch:stock_finder')

@login_required
def profile(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            try:
                # 1. commit=False로 객체 생성
                interest_stock = form.save(commit=False)
                # 2. user 할당
                interest_stock.user_name = request.user
                # 3. 최종 저장
                interest_stock.save()
            # UniqueConstraint 위반 시 오류 발생
            except IntegrityError:
                messages.error(request, '이미 등록된 관심 종목입니다.')
            return redirect('accounts:profile')

    else:
        form = StockForm()
    stocks = UserinterestStock.objects.all()
    context = {
        'stocks': stocks,
        'form': form,
    }
    return render(request, 'accounts/profile.html', context)


def stock_delete(request, pk):
    stock = UserinterestStock.objects.get(pk=pk)
    stock.delete()
    return redirect('accounts:profile')