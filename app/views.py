from django.shortcuts import render, redirect
from .forms import AppBancoForm

def index(request):
    return render(request, "index.html")

def create_appbanco(request):
    if request.method == 'POST':
        form = AppBancoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('index')  # Redireciona para a view 'index' após salvar com sucesso
            except Exception as e:
                print(f"Erro ao salvar o formulário: {e}")
                # Aqui você pode tratar o erro de alguma forma, como exibir uma mensagem de erro para o usuário
        else:
            print(f"Formulário inválido: {form.errors}")
            # Aqui você pode verificar os erros do formulário para depuração

    else:
        form = AppBancoForm()

    return render(request, 'create_appbanco.html', {'form': form})