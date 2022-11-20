from django.contrib.auth.decorators import login_required
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
