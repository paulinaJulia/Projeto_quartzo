from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from ...models import Pagamento


@login_required(login_url='/')
def update_item_pagamento(request, pagamento_pk, item_pagamento_pk):
    pagamento = get_object_or_404(Pagamento, pk=pagamento_pk)

    item = pagamento.items.get(id=item_pagamento_pk)
    item.status = 'aprovado'
    item.save()

    from functions_globais.redirect import reverse_lazy_plus
    return reverse_lazy_plus(url_name='pagamento_detail', url_params=[pagamento_pk], just_uri=False)
