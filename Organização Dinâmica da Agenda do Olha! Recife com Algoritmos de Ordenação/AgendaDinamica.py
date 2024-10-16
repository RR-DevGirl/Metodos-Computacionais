import heapq
from time import time
import math
from datetime import datetime

# MERGE e HEAP -> LISTA COM 8 ELEMENTOS
eventos = [
    ('27/09/2024 09:30', 'Olha! Recife a Pé – Recife Walking Tour'),
    ('28/09/2024 09:00', 'Olha! Recife no Rio – Ilha de Deus'),
    ('28/09/2024 09:00', 'Olha! Recife de Ônibus – Jardim Botânico'),
    ('28/09/2024 14:00', 'Olha! Recife de Ônibus – Instituto Ricardo Brennand'),
    ('29/09/2024 13:00', 'Olha! Recife de Ônibus – Fundação Gilberto Freyre'),
    ('29/09/2024 09:00', 'Olha! Recife Pedalando – Antigos Cinemas do Recife'),
    ('02/10/2024 14:00', 'Olha! Recife a Pé – Pátio do Terço e Arredores'),
    ('04/10/2024 09:30', 'Olha! Recife a Pé – Recife Walking Tour')
]

# MERGE e HEAP -> NOVOS EVENTOS
novos_eventos = [
    ('03/10/2024 10:00', 'Olha! Recife Especial – Tour Cultural'),
    ('04/10/2024 11:00', 'Olha! Recife Histórico – Centro da Cidade'),
    ('05/10/2024 09:00', 'Olha! Recife Gastronômico – Sabores da Cidade')
]

# QUICK -> LISTA COM 8 ELEMENTOS
lista = [
    {"nome": "Olha! Recife a Pé", "data": "27/09/2024", "hora": "09:30", "local": "Recife Walking Tour"},
    {"nome": "Olha! Recife no Rio", "data": "28/09/2024", "hora": "09:00", "local": "Ilha de Deus"},
    {"nome": "Olha! Recife de Ônibus", "data": "28/09/2024", "hora": "09:00", "local": "Jardim Botânico"},
    {"nome": "Olha! Recife de Ônibus", "data": "28/09/2024", "hora": "14:00", "local": "Instituto Ricardo Brennand"},
    {"nome": "Olha! Recife de Ônibus", "data": "29/09/2024", "hora": "13:00", "local": "Fundação Gilberto Freyre"},
    {"nome": "Olha! Recife Pedalando", "data": "29/09/2024", "hora": "09:00", "local": "Antigos Cinemas do Recife"},
    {"nome": "Olha! Recife a Pé", "data": "02/10/2024", "hora": "14:00", "local": "Pátio do Terço e Arredores"},
    {"nome": "Olha! Recife a Pé", "data": "04/10/2024", "hora": "09:30", "local": "Recife Walking Tour"}
]
# QUICK -> LISTA QUICK COM 11 ELEMENTOS
lista_add = [
    {"nome": "Olha! Recife a Pé", "data": "27/09/2024", "hora": "09:30", "local": "Recife Walking Tour"},
    {"nome": "Olha! Recife no Rio", "data": "28/09/2024", "hora": "09:00", "local": "Ilha de Deus"},
    {"nome": "Olha! Recife de Ônibus", "data": "28/09/2024", "hora": "09:00", "local": "Jardim Botânico"},
    {"nome": "Olha! Recife de Ônibus", "data": "28/09/2024", "hora": "14:00", "local": "Instituto Ricardo Brennand"},
    {"nome": "Olha! Recife de Ônibus", "data": "29/09/2024", "hora": "13:00", "local": "Fundação Gilberto Freyre"},
    {"nome": "Olha! Recife Pedalando", "data": "29/09/2024", "hora": "09:00", "local": "Antigos Cinemas do Recife"},
    {"nome": "Olha! Recife a Pé", "data": "02/10/2024", "hora": "14:00", "local": "Pátio do Terço e Arredores"},
    {"nome": "Olha! Recife a Pé", "data": "04/10/2024", "hora": "09:30", "local": "Recife Walking Tour"},
    {"nome": "Olha! Recife Noturno", "data": "01/10/2024", "hora": "21:00", "local": "Tour Histórico"},
    {"nome": "Olha! Recife Pedalando", "data": "29/09/2024", "hora": "09:00", "local": "Antigos Cinemas do Recife"},
    {"nome": "Olha! Recife de Barco", "data": "26/09/2024", "hora": "12:00", "local": "Passeio no Capibaribe"}
]

# MERGESORT
# MERGESORT
# MERGESORT
# Função que converte as strings de data e hora para objetos datetime
def converter_eventos(eventos):
    eventos_convertidos = []
    for data_hora, descricao in eventos:
        data_hora_formatada = datetime.strptime(data_hora, '%d/%m/%Y %H:%M')
        eventos_convertidos.append((data_hora_formatada, descricao))
    return eventos_convertidos

def merge_sort(eventos):
    if len(eventos) > 1:
        mid = len(eventos) // 2  # Encontra o ponto médio da lista
        left_half = eventos[:mid]  # Divide a lista em duas metades
        right_half = eventos[mid:]

        # Recursivamente divide as duas metades
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Mescla as duas metades de volta em eventos
        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] < right_half[j][0]:  # Compara as datas
                eventos[k] = left_half[i]
                i += 1
            else:
                eventos[k] = right_half[j]
                j += 1
            k += 1

        # Verifica se restam elementos na metade esquerda
        while i < len(left_half):
            eventos[k] = left_half[i]
            i += 1
            k += 1

        # Verifica se restam elementos na metade direita
        while j < len(right_half):
            eventos[k] = right_half[j]
            j += 1
            k += 1

# Função para adicionar novos eventos à lista
def adicionar_evento(eventos, novos_eventos):
    for data_hora, descricao in novos_eventos:
        data_hora_formatada = datetime.strptime(data_hora, '%d/%m/%Y %H:%M')
        eventos.append((data_hora_formatada, descricao))

# Função para exibir a lista de eventos formatados
def exibir_eventos(eventos):
    for evento in eventos:
        print(evento[0].strftime('%d/%m/%Y %H:%M'), "-", evento[1])

# Converte os eventos iniciais
eventos_convertidos = converter_eventos(eventos)

# Realiza a ordenação com merge sort
start_time = time()  # Captura o tempo de início
merge_sort(eventos_convertidos)  # Ordena os eventos
end_time = time()  # Captura o tempo final

# Calcula o tempo de execução
tempo_execucao = end_time - start_time
print('MERGESORT:')
print('Lista de 8 elementos organizada:')
exibir_eventos(eventos_convertidos)
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
complex_merge = len(eventos)*math.log2(len(eventos))
print(f'Complexidade - {complex_merge}')

print('\nLista de 11 elementos organizada:')
adicionar_evento(eventos_convertidos, novos_eventos)
# Reordena após a adição
start_time = time()  # Captura o tempo de início
merge_sort(eventos_convertidos)
end_time = time()  # Captura o tempo final
tempo_execucao = end_time - start_time
exibir_eventos(eventos_convertidos)
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
complex_merge = len(eventos_convertidos)*math.log2(len(eventos_convertidos))
print(f'Complexidade - {complex_merge}')

# QUICKSORT
# QUICKSORT
# QUICKSORT
def conv(evento):
  return datetime.strptime(f"{evento['data']} {evento['hora']}", "%d/%m/%Y %H:%M")

def quicksort(eventos, esq, dir):
  if esq < dir:
    particao_pos = particao(eventos, esq, dir)
    quicksort(eventos, esq, particao_pos - 1)
    quicksort(eventos, particao_pos + 1, dir)

def particao(eventos, esq, dir):
  i = esq
  j = dir - 1
  pivo = conv(eventos[dir])

  while i < j:
    while i < dir and conv(eventos[i]) < pivo:
      i += 1
    while j > esq and conv(eventos[j]) >= pivo:
      j -= 1
    if i < j:
      eventos[i], eventos[j] = eventos[j], eventos[i]
  if conv(eventos[i]) > pivo:
    eventos[i], eventos[dir] = eventos[dir], eventos[i]
  return i

ini = time()
quicksort(lista, 0, len(lista) - 1)
fim = time()
complex_quick = len(lista)*math.log2(len(lista))
print('\n\nQUICKSORT:')
print('Lista de 8 elementos organizada:')
for evento in lista:
    print(f"{evento['nome']} - {evento['data']} {evento['hora']} - {evento['local']}")
print(f'Tempo de execução: {fim-ini}')
print(f'Complexidade - {complex_quick}')

ini = time()
quicksort(lista_add, 0, len(lista_add) - 1)
fim = time()
complex_quick = len(lista_add)*math.log2(len(lista_add))
print('\nLista de 11 elementos organizada:')
for evento in lista_add:
    print(f"{evento['nome']} - {evento['data']} {evento['hora']} - {evento['local']}")
print(f'Tempo de execução: {fim-ini} segundos')
print(f'Complexidade - {complex_quick}')


# HEAPSORT
# HEAPSORT
# HEAPSORT
def converter_eventos(eventos):
    eventos_convertidos = []
    for data_hora, descricao in eventos:
        data_hora_formatada = datetime.strptime(data_hora, '%d/%m/%Y %H:%M')
        eventos_convertidos.append((data_hora_formatada, descricao))
    return eventos_convertidos

def heapsort(eventos):
    heapq.heapify(eventos)

    eventos_ordenados = []
    while eventos:
        eventos_ordenados.append(heapq.heappop(eventos))

    return eventos_ordenados

def adicionar_evento(eventos, novos_eventos):
    for data_hora, descricao in novos_eventos:
        data_hora_formatada = datetime.strptime(data_hora, '%d/%m/%Y %H:%M')
        heapq.heappush(eventos, (data_hora_formatada, descricao))

def exibir_eventos(eventos):
    for evento in eventos:
        print(evento[0].strftime('%d/%m/%Y %H:%M'), "-", evento[1])

eventos_convertidos = converter_eventos(eventos)
start_time = time()
eventos_ordenados = heapsort(eventos_convertidos)
end_time = time()
tempo_execucao = end_time - start_time

print('\n\nHEAPSORT:')
print('Lista de 8 elementos organizada:')
exibir_eventos(eventos_ordenados)
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
complex_heap = len(eventos_ordenados)*math.log2(len(eventos_ordenados))
print(f'Complexidade - {complex_heap}')

print('\nLista de 11 elementos organizada:')
adicionar_evento(eventos_ordenados, novos_eventos)
start_time = time()
eventos_ordenados = heapsort(eventos_ordenados)  # Reordena após a adição
end_time = time()
tempo_execucao = end_time - start_time
exibir_eventos(eventos_ordenados)
print(f"Tempo de execução: {tempo_execucao:.6f} segundos")
complex_heap = len(eventos_ordenados)*math.log2(len(eventos_ordenados))
print(f'Complexidade - {complex_heap}')