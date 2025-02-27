from django.shortcuts import render , redirect
from  django.views.generic import CreateView, ListView, UpdateView, DeleteView ,DetailView
from .models import Address
from .forms import AddressForm,CePForm
from django.urls import reverse_lazy
import requests


def cep_search_view(request):
    if request.method == 'POST':
        form = CePForm()

    message = ''

    if request.method == 'POST':
        form = CePForm(request.POST)

        cep_digitado = request.POST.get('cep')
        url = f"https://viacep.com.br/ws/{cep_digitado}/json/"
        response = requests.get(url)

        if response.status == 200:
            dados_cep = response.json()
            if 'erro' in dados_cep:
                message = 'CEP não encontrado'
            else:
                resposta_em_json_filtrada = {
                    'cep': dados_cep['cep'],
                    'logradouro': dados_cep['logradouro'],
                    'bairro': dados_cep['bairro'],
                    'localidade': dados_cep['localidade'],
                    'uf': dados_cep['uf']
                }
                form = CePForm(initial=resposta_em_json_filtrada)
                
                if form.is_valid():
                    form.save(commit=False)
                    form.save()
                    form = CePForm(intial={})
        else:
            message ='Erro durante a requisição da API. Tente novamente mais tarde'
    return render(request, 'endereco/cepSearch.html', {'form': form, 'message': message})

class AddressCreate(CreateView):
    model = Address 
    form_class = AddressForm
    context_object_name = 'CreateAddressForm'
    template_name = 'endereco/address.Form.html'
    success_url = reverse_lazy('endereco:list')

class AddressList(ListView):
    model = Address
    template_name = 'endereco/address.List.html'
    context_object_name = 'address'

# Create your views here.
class AddressUpdate(UpdateView):
    model = Address
    form_class = AddressForm
    context_object_name = 'address'
    template_name = 'endereco/address.Form.html'
    success_url = reverse_lazy('endereco:list')

class AddressDetail(DetailView):
    model = Address
    template_name = 'endereco/address.Detail.html'
    context_object_name = 'address'

class AddressDelete(DeleteView):
    model = Address
    template_name = 'endereco/address.Delete.html'
    context_object_name = 'address'
 