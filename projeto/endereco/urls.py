from django.urls import path
from .views import AddressCreate, AddressList, AddressUpdate,AddressDetail, AddressDelete, cep_search_view

app_name = 'endereco'

urlpatterns = [
    path('criar/', AddressCreate.as_view() , name='criar'),
    path('listar/', AddressList.as_view() , name='listar'),
    path('Detalhar/<int:pk>/', AddressDetail.as_view() , name='Detalhar'),
    path('editar/<int:pk>/', AddressUpdate.as_view() , name='editar'),
    path('deletar/<int:pk>/', AddressDelete.as_view() , name='deletar'),
    path('cep/', cep_search_view, name='cep_search')

]
