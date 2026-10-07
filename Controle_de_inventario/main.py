# Sistema de Controle de Inventário de Equipamentos
from Controle_de_inventario.funcoes_inventario import *

minhalista = []
print('Preenchendo')
preeccherinventario(minhalista)
print('Exibindo')
exibirinventario(minhalista)

print('Pesquisando')
localizarpornome(minhalista)
print('Alterando')
depreciarpornome(minhalista)

print('Excluindo')
excluirporserial(minhalista)
exibirinventario(minhalista)

print('Resumindo')
resumirvalores(minhalista)
