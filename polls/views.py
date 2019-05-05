from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hoşgeldin kardo.")

def detail(request,soru_id):
    return HttpResponse("Şu sorulara bakıyorsunuz %s" %soru_id)


def results(request,soru_id):
    return HttpResponse("Şu soruların cevaplarına bakyorsunuz %s" %soru_id)


def index(request,soru_id):
    return HttpResponse("Bu soruyu yanıtlıyorsunuz %s" %soru_id)


# Create your views here.
