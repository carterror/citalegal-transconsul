from django.contrib.auth.decorators import login_required as original_login_required
from django.contrib.admin.views.decorators import staff_member_required as original_staff_member_required
from django.contrib import messages
from functools import wraps
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse


def login_required(view_func):

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, 'Debe estar autenticado')
            return original_login_required(view_func)(request, *args, **kwargs)
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view


def staff_member_required(view_func):

    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff:
            messages.info(request, 'Debe ser administrador')
            return redirect(reverse_lazy('home'))
        return view_func(request, *args, **kwargs)
    
    return _wrapped_view