from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.core.paginator import Paginator
from .models import Contatos
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
# Create your views here.


def index(request):
    #messages.add_message(request, messages.ERROR, 'Error de teste')
    contatos = Contatos.objects.order_by('-id').filter(
        ativo=True
    )
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def detalhe(request, vid):
    #contato = Contatos.objects.get(id=vid)
    contato = get_object_or_404(Contatos, id=vid)
    if not contato.ativo:
        raise Http404()
    return render(request, 'contatos/detalhe.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        return redirect('index')

    campos = Concat('nome', Value(' '), 'sobrenome')
    contatos = Contatos.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
        ativo=True
    )
    paginator = Paginator(contatos, 10)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
