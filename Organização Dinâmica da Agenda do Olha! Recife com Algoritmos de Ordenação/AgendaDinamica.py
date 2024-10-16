import math
from time import time
from datetime import datetime
import heapq


def conv(evento):
    # Acessa o segundo elemento da tupla que é o dicionário do evento
   return  datetime.strptime(f"{evento['data']} {evento['hora']}", "%d/%m/%Y %H:%M")
     

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


def heapsort(eventos):
    # Criação de uma lista de eventos formatados como tuplas (data_hora, evento)
    eventos_formatados = [(conv(evento), evento) for evento in eventos]
    heapq.heapify(eventos_formatados)

    eventos_ordenados = []
    while eventos_formatados:
        eventos_ordenados.append(heapq.heappop(eventos_formatados)[1])  # Apenas o dicionário

    return eventos_ordenados


def adicionar_evento(eventos, novos_eventos):
    for evento in novos_eventos:
        # Criação de uma tupla (data_hora, evento) para inserção no heap
        heapq.heappush(eventos, (conv(evento), evento))


def remover_evento(eventos, descricao):
    eventos[:] = [evento for evento in eventos if evento[1]['nome'] != descricao]
    heapq.heapify(eventos)


def exibir_eventos(eventos):
    for evento in eventos:
        print(f"{evento['data']} {evento['hora']} - {evento['nome']} - {evento['local']}")


# Lista inicial de eventos
lista = [
    {
        "nome": "Olha! Recife a Pé",
        "data": "27/09/2024",
        "hora": "09:30",
        "local": "Recife Walking Tour",
    },
    {
        "nome": "Olha! Recife no Rio",
        "data": "28/09/2024",
        "hora": "09:00",
        "local": "Ilha de Deus",
    },
    {
        "nome": "Olha! Recife de Ônibus",
        "data": "28/09/2024",
        "hora": "09:00",
        "local": "Jardim Botânico",
    },
    {
        "nome": "Olha! Recife de Ônibus",
        "data": "28/09/2024",
        "hora": "14:00",
        "local": "Instituto Ricardo Brennand",
    },
    {
        "nome": "Olha! Recife de Ônibus",
        "data": "29/09/2024",
        "hora": "13:00",
        "local": "Fundação Gilberto Freyre",
    },
    {
        "nome": "Olha! Recife Pedalando",
        "data": "29/09/2024",
        "hora": "09:00",
        "local": "Antigos Cinemas do Recife",
    },
    {
        "nome": "Olha! Recife a Pé",
        "data": "02/10/2024",
        "hora": "14:00",
        "local": "Pátio do Terço e Arredores",
    },
    {
        "nome": "Olha! Recife a Pé",
        "data": "04/10/2024",
        "hora": "09:30",
        "local": "Recife Walking Tour",
    },
]

# Ordenação inicial com QuickSort
ini = time()
quicksort(lista, 0, len(lista) - 1)
fim = time()
complex_quick = len(lista) * math.log2(len(lista))
print("Lista Organizada:")
exibir_eventos(lista)
print(f"Tempo de execução: {fim - ini:.6f} segundos")
print(f"Complexidade - {complex_quick:.2f}")

# Lista de novos eventos a serem adicionados
lista_add = [
    {
        "nome": "Olha! Recife Noturno",
        "data": "01/10/2024",
        "hora": "21:00",
        "local": "Tour Histórico",
    },
    {
        "nome": "Olha! Recife Pedalando",
        "data": "29/09/2024",
        "hora": "09:00",
        "local": "Antigos Cinemas do Recife",
    },
    {
        "nome": "Olha! Recife de Barco",
        "data": "26/09/2024",
        "hora": "12:00",
        "local": "Passeio no Capibaribe",
    },
]

# Convertendo a lista original de eventos para a estrutura de tupla
eventos_convertidos = [(conv(evento), evento) for evento in lista]

# Adicionando novos eventos
print("\nAdicionando novos eventos:")
adicionar_evento(eventos_convertidos, lista_add)
eventos_convertidos = heapsort(eventos_convertidos)  # Reordena após a adição
exibir_eventos(eventos_convertidos)

# Removendo um evento
print("\nRemovendo evento:")
remover_evento(eventos_convertidos, "Olha! Recife no Rio")
eventos_convertidos = heapsort(eventos_convertidos)  # Reordena após a remoção
exibir_eventos(eventos_convertidos)
from datetime import datetime
import time

# Lista de eventos com data e descrição
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

# Função que converte as strings de data e hora para objetos datetime
def converter_eventos(eventos):
    eventos_convertidos = []
    for data_hora, descricao in eventos:
        data_hora_formatada = datetime.strptime(data_hora, '%d/%m/%Y %H:%M')
        eventos_convertidos.append((data_hora_formatada, descricao))
    return eventos_convertidos

# Implementação do merge sort
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

# Função para remover um evento específico pela descrição
def remover_evento(eventos, descricao):
    eventos[:] = [evento for evento in eventos if evento[1] != descricao]

# Função para exibir a lista de eventos formatados
def exibir_eventos(eventos):
    for evento in eventos:
        print(evento[0].strftime('%d/%m/%Y %H:%M'), "-", evento[1])

# Converte os eventos iniciais
eventos_convertidos = converter_eventos(eventos)

# Realiza a ordenação com merge sort
start_time = time.time()  # Captura o tempo de início
merge_sort(eventos_convertidos)  # Ordena os eventos
end_time = time.time()  # Captura o tempo final

# Calcula o tempo de execução
tempo_execucao = end_time - start_time
print(f"Tempo de execução do merge sort: {tempo_execucao:.6f} segundos")
print(f"Eventos ordenados inicialmente:")
exibir_eventos(eventos_convertidos)

# Adicionando três novos eventos
novos_eventos = [
    ('03/10/2024 10:00', 'Olha! Recife Especial – Tour Cultural'),
    ('04/10/2024 11:00', 'Olha! Recife Histórico – Centro da Cidade'),
    ('05/10/2024 09:00', 'Olha! Recife Gastronômico – Sabores da Cidade')
]

print("\nAdicionando novos eventos:")
adicionar_evento(eventos_convertidos, novos_eventos)

# Reordena após a adição
merge_sort(eventos_convertidos)
exibir_eventos(eventos_convertidos)

# Removendo um evento
print("\nRemovendo evento:")
remover_evento(eventos_convertidos, 'Olha! Recife no Rio – Ilha de Deus')

# Reordena após a remoção
merge_sort(eventos_convertidos)
exibir_eventos(eventos_convertidos)
