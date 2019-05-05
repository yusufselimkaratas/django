from django.shortcuts import render

from django.http import HttpResponse

from .models import Sorular


def index(request):
    son_soru_listesi=Sorular.objects.order_by('-tarih')[:5]
    output=', '.join([q.soru_metni for q in son_soru_listesi])
        return HttpResponse(output)

def detail(request,soru_id):
    return HttpResponse("Şu sorulara bakıyorsunuz %s" %soru_id)


def results(request,soru_id):
    return HttpResponse("Şu soruların cevaplarına bakyorsunuz %s" %soru_id)


def index(request,soru_id):
    return HttpResponse("Bu soruyu yanıtlıyorsunuz %s" %soru_id)


# Create your views here.
