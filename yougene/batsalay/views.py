from django.shortcuts import render
from django.http import HttpResponse


def index(request):
       host = request.META['HTTP_HOST']
       user_agent = request.META['HTTP_USER_AGENT']
       path = request.path

       text = f' host: {host}, briwser: {user_agent}, path: {path}'
       return HttpResponse(text, headers={"SecretCode": "123141"})

def user(request, name = 'Noname', age=0):
       return HttpResponse(f'User: {name}. his age {age}')