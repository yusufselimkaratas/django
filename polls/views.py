from django.shortcuts import render
from django.http import Http404

from django.http import HttpResponse

from .models import Sorular


def index(request):
    son_soru_listesi=Sorular.objects.order_by('-tarih')[:5]

    context = {'son_soru_listesi':son_soru_listesi,}
    output=', '.join([q.soru_metni for q in son_soru_listesi])
    return render(request, 'polls/index.html',context)

def detail(request,soru_id):
    try:
        soru=Sorular.objects.get(pk=soru_id)
    except Sorular.DoesNotExist:
        raise Http404("Soru Mecvut Değil Hocam")

    return render(request, 'polls/detail.html',{'question':soru})


def results(request,soru_id):
    return HttpResponse("Şu soruların cevaplarına bakyorsunuz %s" %soru_id)


def vote(request,soru_id):
    return HttpResponse("Bu soruyu yanıtlıyorsunuz %s" %soru_id)


# Create your views here.
