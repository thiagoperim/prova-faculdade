from django.shortcuts import render
from rest_framework import generics

from .forms import ContatoForm
from .models import Contato
from .serializers import ContatoSerializer


def contato_view(request):
    success_message = None
    error_message = None

    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = 'Cadastro enviado com sucesso!'
            form = ContatoForm()
        else:
            error_message = 'Ocorreu um erro ao enviar o formulário. Verifique os campos obrigatórios.'
    else:
        form = ContatoForm()

    context = {
        'form': form,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'faleconosco/contato.html', context)


class ContatoListAPIView(generics.ListAPIView):
    # só lista tudo em json
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
