from django.shortcuts import render
from .new_releases import Serve


def show_homepage(request):
    return render(
        request=request,
        template_name='home.html',
    )


def show_menu(request):
    return render(
        request=request,
        template_name='menu.html',
    )


def show_new_music(request):
    server1 = Serve()

    return render(
        request=request,
        template_name='new_music.html',
        context={
            'artists': server1.serve_new_releases()
        }
    )


def show_sotw(request):
    return render(
        request=request,
        template_name='sotw.html',
    )


def show_about(request):
    return render(
        request=request,
        template_name='about.html',
    )