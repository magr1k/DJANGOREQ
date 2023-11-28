from django.shortcuts import render
from django.http import HttpResponse

def base(request):
    h = request.META['HTTP_HOST']
    ua = request.META['HTTP_USER_AGENT']

    text = f' host: {h}, browser: {ua}'
    return HttpResponse(text)

def error(request):
    return HttpResponse('Произошла непредвиденная ошибка', status=404, reason='not found')


def user(request, login='Nologin', post='Nopost', num=0):
    return HttpResponse(f'User: user login: {login}. his post: {post}, his number: {num}')


