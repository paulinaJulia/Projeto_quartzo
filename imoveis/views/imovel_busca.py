from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from ..models import Imovel

@login_required
def imovel_busca(request):
    context = {
        'object_list': Imovel.objects.filter(categoria__iexact= request.GET.get('categoria'))
    }

    return render(
        request,
        'imovel_list_view.html',
        context
    )

@login_required
def search_imoveis(request):
    search = request.GET.get('busca')
    context = {
        'list': Imovel.objects.filter(Q(categoria__iexact=search) | Q(rua__iexact=search) | Q(bairro__iexact=search) | Q(cidade__iexact=search))
    }

    return render(request, template_name='core/index.html', context=context)