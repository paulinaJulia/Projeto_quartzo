from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from imoveis.models import Imovel

@login_required
def home(request):
    context = {
        'list': Imovel.objects.all().order_by('-id')[0:5]
    }
    
    return render(request, context=context, template_name='core/index.html')