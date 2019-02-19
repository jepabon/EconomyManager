from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Movimiento

@login_required
def reporte_gastos(request):
    from django.db.models import Sum, CharField, Value, F
    from django.db.models.functions import Coalesce, Concat

    movimientos = Movimiento.objects.filter(created_by=request.user).values('categoria').\
        annotate(total=Sum('valor'))

    for m in movimientos:
        m['categoria'] = movimientos.model(categoria=m['categoria']).get_categoria_display()

    context = {}
    context['site_header'] = "Informe de Gastos"
    context['has_permission'] = True
    context['movimientos'] = movimientos

    return render(request, 'gastos.html', context=context)
